from collections import defaultdict
from datetime import date, datetime
from os.path import splitext
import hashlib
import os


class image_manager(object):
    def __init__(self, input_dir: str, output_dir: str, task: int):
        self.ignore_extensions = [".DS_Store"]
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.task = task

    def run(self):
        print(self.input_dir)
        print(self.output_dir)
        if self.task == 1:
            print("查找重复文件（新文件视为重复文件）")
            self.find_duplicate_files("asc")
        elif self.task == 2:
            print("查找重复文件（旧文件视为重复文件）")
            self.find_duplicate_files("desc")
        elif self.task == 3:
            print("将文件按年月归类")
            self.categorizer_by_month()
        else:
            raise Exception("未知任务")

    def get_file_body(self, path: str):
        with open(path, "rb") as f:
            return f.read()

    def get_all_files_in_dir(self):
        full_paths = []
        for path, subdirs, files in os.walk(self.input_dir):
            for name in files:
                extension = splitext(name)[1]
                if extension in self.ignore_extensions:
                    continue
                full_paths.append(os.path.join(path, name))
        return full_paths

    def find_duplicate_files(self, order: str = "asc"):
        full_paths = self.get_all_files_in_dir()
        full_paths_with_timestamp = []
        for full_path in full_paths:
            timestamp = os.path.getmtime(full_path)
            date_time = datetime.fromtimestamp(timestamp)
            full_paths_with_timestamp.append(
                {
                    "full_path": full_path,
                    "date_time": date_time,
                }
            )
        full_paths_with_timestamp.sort(
            key=lambda x: x["date_time"], reverse=order == "desc"
        )

        hash_set = set()
        for full_path in full_paths_with_timestamp:
            body = self.get_file_body(full_path)
            v = hashlib.sha256(body).hexdigest()
            if v in hash_set:
                print(full_path)
            else:
                hash_set.add(v)
        print("查找完成")

    def categorizer_by_month(self):
        full_paths = self.get_all_files_in_dir()

        # 按年月归类
        year_month_files = defaultdict(lambda: defaultdict(list))
        for full_path in full_paths:
            timestamp = os.path.getmtime(full_path)
            date_time = datetime.fromtimestamp(timestamp)
            year = date.strftime(date_time, "%Y")
            month = date.strftime(date_time, "%m")
            year_month_files[year][month].append(full_path)

        # 创建文件夹
        for year, months in year_month_files.items():
            for month, files in months.items():
                path = os.path.join(self.output_dir, year, month)
                if not os.path.exists(path):
                    os.makedirs(path)
        print("创建文件夹完成")

        # 移动文件
        for year, months in year_month_files.items():
            for month, files in months.items():
                for file in files:
                    path = os.path.join(self.output_dir, year, month)
                    os.rename(file, os.path.join(path, os.path.basename(file)))
        print("移动文件完成")
