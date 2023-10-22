# JSON File Splitter for LastFM


A Python script designed to split large JSON files into smaller chunks, ensuring each section conforms to a predefined structure.

## Features

- ### **UTF-8 Encoding**: Handles a wide range of characters by reading the input JSON file using UTF-8 encoding.

- ### **Consistent Structure**: If any fields are missing from a section in the input file, the script will add them with a default value of "MISSING".

- ### **Flexible Splitting**: Splits the input file into chunks of a specified number of sections (default is 2000 sections).

- ### **Command-Line Interface**: Easily run the script from the command line.

## Usage

1. Clone the repository:

```bash
git clone <https://github.com/Gvmmx/json-splitter-for-lastFM>
cd <repository-directory>
```
2. Run the script:


```bash
python splitter.py <path_to_json_file> <output_directory>
```

Replace <path_to_json_file> with the path to your JSON file and <output_directory> with the directory where you want the split files to be saved.




# Getting Your Extended Streaming History on Spotify

Follow these steps to download your extended streaming history from Spotify:

1. **Visit Spotify's Data Privacy Page**:

   - Open a web browser and go to [Spotify Data Privacy](https://www.spotify.com/account/privacy/)

2. **Log In**:

   - If prompted, log in to your Spotify account with your username and password.

3. **Access Your Data**:

   - Scroll down to the section titled "Download your data" and click on the "Request" button.

5. **Confirmation**:

   - Spotify will confirm that they are processing your request and will let you know via email when your data is ready for download.

6. **Check Your Email**:

   - After some time, you'll receive an email from Spotify informing you that your data is ready for download. This may take a few days.

7. **Download Your Data**:

   - Click on the link provided in the email to download your data.

8. **Extract and Explore**:

   - You'll likely receive a zip file. Extract it to access your data. Inside, you'll find various files containing information about your Spotify activity.
