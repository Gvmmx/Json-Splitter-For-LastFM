JSON File Splitter for LastFM

Description:
This script is designed to split a large JSON file into smaller JSON files, each containing a specified maximum number of sections (default is set to 2000 sections). The script ensures that each section in the output files conforms to a predefined structure, filling in any missing fields with a default value of "MISSING".

Key Features:

UTF-8 Encoding: The script reads the input JSON file using the UTF-8 encoding to handle a wide range of characters.

Default Structure: The script ensures that each section in the output files has a consistent structure. If any fields are missing from a section in the input file, the script will add them with a default value of "MISSING".

Flexible Splitting: By default, the script splits the input file into chunks of 2000 sections each, but this number can be adjusted if needed.

Command-Line Interface: The script is designed to be run from the command line and accepts two arguments: the path to the input JSON file and the directory where the split files should be saved.

How It Works:

The script starts by checking if the provided arguments are correct. If not, it provides the user with the correct usage format.

It then reads the input JSON file, ensuring that the data is a list of sections.

For each chunk of sections (up to the specified maximum), the script:

Ensures that the chunk conforms to the predefined structure.
Saves the chunk to a new JSON file in the specified output directory.
The script provides feedback to the user, indicating the start of the splitting process and its successful completion.

If any errors occur during execution, the script will print an error message to help diagnose the issue.

Usage:
To use the script, navigate to its directory in the command prompt and run:

"" python splitter.py <path_to_json_file> <output_directory> ""

Replace <path_to_json_file> with the path to your JSON file and <output_directory> with the directory where you want the split files to be saved.

