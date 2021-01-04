## About
![PyPI](https://img.shields.io/pypi/v/metamore)

Metamore is a command line tool that helps you manage your metadata. Powered by [Piexif](https://github.com/hMatoba/Piexif). If you'd like to contribute to development, please read on how to get started with [Poetry](https://python-poetry.org) packaging system.

## Usage

To install Metamore simply run: `pip install metamore`. If `pip` recommends you to add the directory where Metamore was installed to PATH, do so.

### Options

- get - Get EXIF metadata from file(s)
- remove - Remove all EXIF metadata from file(s)
- transfer - Transfer EXIF metadata from one file to another

### Examples

After installation and adding install directory to PATH Metamore is ready to go. Here is a couple of examples of the commands you can run:
- `mm get -o Canon_40D.jpg` - Will save all the EXIF metadata found in the file 'Canon_40D.jpg' to a text file.
- `mm remove -d Pictures/` - Will remove all the EXIF metadata from all the .jpg/.jpeg files in the directory 'Pictures'.
- `mm transfer Canon_40D.jpg Nikon_D70.jpg` - Will transfer EXIF metadata from the first file to the second one.

## ToDo

- [x] Remove metadata from all files in the directory
- [ ] Listen for new files in the directory and automatically remove their metadata
