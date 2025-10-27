# Barcode Generator

A simple Python tool to generate Code-128 barcodes from any URL (especially bit.ly shortened links).

## Features

- ✅ Generate Code-128 barcodes from any URL
- ✅ Support for command-line arguments
- ✅ Interactive mode if no arguments provided
- ✅ Automatic filename generation
- ✅ Clean and easy-to-use interface

## Installation

### Requirements

- Python 3.6 or higher
- pip (Python package installer)

### Setup

1. Clone this repository:
```bash
git clone https://github.com/yourusername/BarCodeApp.git
cd BarCodeApp
```

2. Install the required packages:
```bash
pip install python-barcode[images]
```

Or install from requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

### Method 1: Command Line Argument

Pass the URL as an argument when running the script:

```bash
python generate_barcode.py http://bit.ly/43H6c6D
```

### Method 2: Interactive Mode

Run the script without arguments and enter the URL when prompted:

```bash
python generate_barcode.py
```

Then enter your URL when prompted:
```
Enter your bit.ly URL (or any URL): http://bit.ly/yourlink
```

### Examples

Generate a barcode for a bit.ly link:
```bash
python generate_barcode.py http://bit.ly/43H6c6D
```
Output: `http___bit_ly_43H6c6D_barcode.png`

Generate a barcode for any URL:
```bash
python generate_barcode.py https://www.example.com
```
Output: `https___www_example_com_barcode.png`

## How It Works

1. The script encodes your URL into a Code-128 barcode
2. Code-128 is a widely supported barcode format that can be scanned by most barcode readers
3. The barcode image is saved as a PNG file
4. The filename is automatically generated from the URL (special characters are replaced with underscores)

## Notes

- The barcode can be scanned by any standard barcode scanner
- The scanned data will be the URL you provided
- Filenames are sanitized to ensure cross-platform compatibility
- The output image will be saved in the same directory as the script

## Requirements

- python-barcode 0.16.1 or higher
- Pillow (PIL) - image processing library
- Python 3.6+

## Project Structure

```
BarCodeApp/
├── generate_barcode.py    # Main script
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome!

## Author

Created with ❤️ by red1

