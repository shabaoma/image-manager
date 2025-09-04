# File Organizer

A simple and easy-to-use file organization tool to help you organize and clean up your files.

## Features

- 🔍 **Find Duplicate Files**: Identify duplicate files through file content hash values
- 📅 **Organize by Year/Month**: Automatically organize files by creation time into year/month folders
- 🚀 **Simple to Use**: Interactive command-line interface with no complex configuration needed

## System Requirements

- Python 3.6 or higher
- Compatible with Windows, macOS, and Linux

## Installation & Usage

### 1. Download the Project

```bash
git clone https://github.com/your-username/file-organizer.git
cd file-organizer
```

### 2. Run the Program

```bash
python main.py
```

## Usage Instructions

After running the program, follow the prompts to enter the following information:

### 1. Input Directory
Enter the path to the source directory containing your files, for example:
```
/Users/username/Downloads/Files
```

### 2. Output Directory
Enter the path to the directory where you want to store the processed results, for example:
```
/Users/username/Documents/Organized
```

### 3. Select Task
The program will display three options, enter the corresponding number:

- **1** - Find duplicate files (newer files considered duplicates)
  - Keeps the earliest created file, marks newer duplicates
  - Suitable for keeping original files and cleaning up subsequent duplicates

- **2** - Find duplicate files (older files considered duplicates)
  - Keeps the latest created file, marks older duplicates
  - Suitable for keeping the latest version and cleaning up old versions

- **3** - Organize files by year/month
  - Automatically creates year/month folders and moves files based on modification time
  - Folder structure: `output_directory/year/month/filename`

## Usage Example

```
Input Directory
/Users/username/Downloads/Files

Output Directory
/Users/username/Documents/Organized

1 Find duplicate files (newer files considered duplicates)
2 Find duplicate files (older files considered duplicates)
3 Organize files by year/month
3
```

## Important Notes

⚠️ **Important Reminders**:
- The program will directly move files, please backup important data before running
- The duplicate file finder will display paths and creation times of duplicate files but won't automatically delete them
- The year/month organizer will move files to a new directory structure
- The program automatically ignores system files like `.DS_Store`

## Supported File Formats

The program supports all file types:
- Image files: JPG, PNG, GIF, BMP, TIFF, etc.
- Video files: MP4, AVI, MOV, etc.
- Document files: PDF, DOC, TXT, etc.
- Audio files: MP3, WAV, FLAC, etc.
- Archive files: ZIP, RAR, 7Z, etc.
- Any other file types

## Technical Details

- **Duplicate Detection**: Uses SHA-256 hash algorithm to calculate file content, ensuring accurate duplicate identification
- **File Organization**: Based on file modification time (mtime) for year/month classification
- **Recursive Scanning**: Automatically scans all subdirectories within the input directory

## Troubleshooting

### Common Issues

1. **Permission Errors**
   - Ensure you have read/write permissions for input and output directories
   - You may need to use `sudo` on macOS/Linux

2. **Path Does Not Exist**
   - Make sure the entered directory paths exist and are correct
   - Use absolute paths to avoid path errors

3. **File in Use**
   - Ensure files to be processed are not open in other applications
   - Close applications that might be using the files

## Contributing

Issues and Pull Requests are welcome to improve this project!

## License

MIT License
