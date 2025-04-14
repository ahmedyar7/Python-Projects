import os
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List


def search_files(
    path: str, search_term: str, mode: str, results: List[str], lock: threading.Lock
) -> None:
    """
    Search for files based on the mode:
    - 'filename': Search by filename (full or partial match)
    - 'extension': Search by file extension
    - 'keyword': Search by content inside files
    """
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            # Search by filename
            if mode == "filename" and search_term in file:
                with lock:
                    results.append(file_path)

            # Search by file extension
            elif mode == "extension" and file.endswith(search_term):
                with lock:
                    results.append(file_path)

            # Search by keyword in file contents
            elif mode == "keyword":
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line in f:
                            if search_term in line:
                                with lock:
                                    results.append(file_path)
                                break  # Stop reading after the first match
                except (UnicodeDecodeError, PermissionError):
                    continue


def get_subdirectories(path: str) -> List[str]:
    """Get top-level subdirectories for multithreading."""
    return [
        os.path.join(path, d)
        for d in os.listdir(path)
        if os.path.isdir(os.path.join(path, d))
    ]


def main(path: str, search_term: str, mode: str) -> None:
    """
    Main function to manage the file search with multithreading.
    """
    # Shared resources and Lock for thread-safe access
    all_matches = []
    lock = threading.Lock()

    # Get top-level subdirectories
    subdirs = get_subdirectories(path)
    if not subdirs:
        subdirs = [path]  # If no subdirs, use the main path

    # Multithreading with ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(
            lambda subdir: search_files(subdir, search_term, mode, all_matches, lock),
            subdirs,
        )

    # Display search results
    if all_matches:
        print("\nSearch Results:")
        for match in all_matches:
            print(match)
    else:
        print("\nNo matching files found.")


# Example Usage
if __name__ == "__main__":
    path = r"/"
    search_term = ".csv"  # Change this to the desired search term
    mode = "extension"  # Options: 'filename', 'extension', 'keyword'
    main(path, search_term, mode)
