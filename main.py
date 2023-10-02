from image_manager import image_manager


input_dir = input("输入目录\n")
output_dir = input("输出目录\n")
task = int(
    input(
        "\n".join(
            [
                "1 查找重复文件（新文件视为重复文件）",
                "2 查找重复文件（旧文件视为重复文件）",
                "3 将文件按年月归类\n",
            ]
        )
    )
)

my_image_manager = image_manager(input_dir, output_dir, task)
my_image_manager.run()
