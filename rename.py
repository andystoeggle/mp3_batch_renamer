#!/usr/bin/env python3
import sys
import os
import string
from pathlib import Path
from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError

def rename_mp3_files(path: str):
    folder = Path(path)
    index = 1

    print(f"Renaming MP3 files in folder: {folder.resolve()}...")

    for file in sorted(folder.glob("*.mp3")):
        try:
            tags = EasyID3(file)
        except ID3NoHeaderError:
            tags = EasyID3()  # file has no ID3 tag

        # Set the title to the filename without the extension
        name_stripped = file.stem.strip(string.digits + string.punctuation + string.whitespace + "-")
        tags["title"] = str(index).zfill(2) + " - " + name_stripped

        # Set the track number based on the order of the files in the folder
        tags["tracknumber"] = str(index)
        index += 1

        tags.save(file, v2_version=3)  # ID3v2.3 is the most widely compatible with phones
        print(f"{file.name:<40.40} -> Title: {tags['title'][0]:<40.40}")

    print("Renaming completed.")

if __name__ == "__main__":
    # Check if a path argument is provided, otherwise use the current directory
    if len(sys.argv) > 1:
        rename_mp3_files(sys.argv[1])
    else:
        rename_mp3_files(os.getcwd())