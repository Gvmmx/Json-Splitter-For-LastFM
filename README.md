# JSON File Splitter


A Python script designed to split large JSON files into smaller chunks, ensuring each section conforms to a predefined structure.

## Features

- ### **UTF-8 Encoding**: Handles a wide range of characters by reading the input JSON file using UTF-8 encoding.

- ### **Consistent Structure**: If any fields are missing from a section in the input file, the script will add them with a default value of "MISSING".

- ### **Flexible Splitting**: Splits the input file into chunks of a specified number of sections (default is 2000 sections).

- ### **Command-Line Interface**: Easily run the script from the command line.

## Usage

1. Clone the repository:

```bash
git clone <repository-url>
cd <repository-directory>
```
2. Run the script:


```bash
python splitter.py <path_to_json_file> <output_directory>
```

Replace <path_to_json_file> with the path to your JSON file and <output_directory> with the directory where you want the split files to be saved.
