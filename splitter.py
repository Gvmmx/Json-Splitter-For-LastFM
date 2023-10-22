import json
import os
import sys

def split_json_file(input_file, output_dir, max_sections=3000):
    print("Starting the split process...")

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Load the JSON data with utf-8 encoding
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Check if the data is a list
    if not isinstance(data, list):
        raise ValueError("The JSON file should contain a list of sections.")

    # Define the default structure
    default_structure = {
        "ts": "MISSING",
        "username": "MISSING",
        "platform": "MISSING",
        "ms_played": "MISSING",
        "conn_country": "MISSING",
        "ip_addr_decrypted": "MISSING",
        "user_agent_decrypted": "MISSING",
        "master_metadata_track_name": "MISSING",
        "master_metadata_album_artist_name": "MISSING",
        "master_metadata_album_album_name": "MISSING",
        "spotify_track_uri": "MISSING",
        "episode_name": "MISSING",
        "episode_show_name": "MISSING",
        "spotify_episode_uri": "MISSING",
        "reason_start": "MISSING",
        "reason_end": "MISSING",
        "shuffle": "MISSING",
        "skipped": "MISSING",
        "offline": "MISSING",
        "offline_timestamp": "MISSING",
        "incognito_mode": "MISSING"
    }

    # Split the data into chunks and save each chunk to a separate file
    for i in range(0, len(data), max_sections):
        chunk = data[i:i + max_sections]
        
        # Ensure each section in the chunk has the desired structure
        for section in chunk:
            for key, default_value in default_structure.items():
                section.setdefault(key, default_value)

        output_file = os.path.join(output_dir, f"split_{i//max_sections + 1}.json")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(chunk, f, indent=4)

    print(f"Split completed. Check the directory {output_dir} for the split files.")

if __name__ == "__main__":
    try:
        if len(sys.argv) != 3:
            print("Usage: python script_name.py <path_to_json_file> <output_directory>")
            sys.exit(1)

        input_file_path = sys.argv[1]
        output_directory = sys.argv[2]

        print(f"Input file: {input_file_path}")
        print(f"Output directory: {output_directory}")

        split_json_file(input_file_path, output_directory)
    except Exception as e:
        print(f"An error occurred: {e}")
