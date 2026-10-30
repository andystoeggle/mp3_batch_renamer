# mp3 Batch Renamer

Set various ID3 tags for all mp3 files in a folder based on their filename.

## Setup

Create a virtual environment and install the dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Afterwards, change the code in `rename.py` to your liking. The default behavior is to set the title tag to the filename without the extension, and the tracknumber tag to the index of the file in the folder (starting from 1).

## Usage

Run the script with the folder path as an argument:

```bash
python rename.py /path/to/folder
```

or simply run it without arguments to rename files in the current working directory:

```bash
python rename.py
```
