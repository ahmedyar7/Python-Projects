# Multithreaded File Search Utility

This Python script performs a multithreaded search for files within a directory and its subdirectories. It allows searching by filename, file extension, or keyword inside the file content. The script uses Python's `os`, `threading`, and `concurrent.futures` modules to efficiently search through large directory trees.

## Features

- 🔍 **Search by filename** (full or partial match)
- 🧩 **Search by file extension**
- 🧠 **Search by keyword inside file contents**
- ⚡ **Multithreaded execution** using `ThreadPoolExecutor` for faster searching
- 🔐 Thread-safe result storage using `threading.Lock`

---

## How It Works

The script:

1. Takes a root directory path, a search term, and a search mode.
2. Uses multithreading to process top-level subdirectories in parallel.
3. Searches through each file according to the selected mode:
   - **Filename mode**: Matches the search term with the file name.
   - **Extension mode**: Matches file extensions like `.txt`, `.csv`, etc.
   - **Keyword mode**: Reads file content and checks for the presence of the search term.

---

## Usage

### Run the Script

Make sure you're in the directory containing the script, then run:

```bash
python main.py
```

Edit the `__main__` section of the script to set:

```python
path = r"/"  # Root path to start searching (e.g., "C:/Users/yourname/Documents")
search_term = ".csv"  # Term to search for (can be part of a filename, extension, or keyword)
mode = "extension"  # Choose one: 'filename', 'extension', 'keyword'
```

### Example

To search for all `.csv` files in your home directory:

```python
path = r"/home/username"
search_term = ".csv"
mode = "extension"
```

---

## Output

Results are printed in the console:

```
Search Results:
/home/username/data/report.csv
/home/username/backup/old_data.csv
```

If no files match:

```
No matching files found.
```

---

## Notes

- 🛡️ The script handles errors like unreadable or binary files (e.g., due to permissions or encoding issues).
- 🧵 Only top-level subdirectories are processed in separate threads. Nested directories are handled serially within each thread's task.
- 🗂️ Works on both Windows and UNIX-like systems (Linux, macOS).

---

## Dependencies

No external libraries required. Uses only the Python standard library:

- `os`
- `threading`
- `concurrent.futures`
- `typing`
