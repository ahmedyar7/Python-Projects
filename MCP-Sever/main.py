from mcp.server.fastmcp import FastMCP
import os

# Create MCP Server
mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__), "notes.txt")


def ensure_file():
    """This would make sure that file actually
    exist before we start to use it"""

    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")


# Creation of mcp-tool
# This function would be the tool that our ai agent could use
# We can pass as many argument as we want but we want to make sure that
# all the parameters have there datatype defined
# Defining the Doc String also very very important


@mcp.tool()
def add_notes(msg: str) -> str:
    """
    Append add new note to sticky note file

    Args:
        msg (str): The note content to be added

    Returns:
        str: Confirmation message indicating the note was saved
    """
    ensure_file()

    with open(NOTES_FILE, "a") as f:
        f.write(msg + "\n")

    return "NOTE SAVED!"


@mcp.tool()
def read_notes() -> str:
    """
    Reads and return all the notes from the sticky notes file

    Returns:
        str: All notes in a single string seperated by the line breaks
        If no notes exists, a default message is returned
    """

    ensure_file()
    with open(NOTES_FILE, "r") as f:
        contents = f.read().strip()

    return contents or "Notes notes yet"


@mcp.tool()
def delete_all_notes() -> str:
    """
    Deletes all the notes in the sticky notes file.

    Returns:
        str: Confirmation message after deleting all notes.
    """
    ensure_file()
    with open(NOTES_FILE, "w") as f:
        f.write("")
    return "All notes have been deleted."


@mcp.tool()
def search_notes(keyword: str) -> str:
    """
    Searches for a keyword in all notes.

    Args:
        keyword (str): The keyword to search for in the notes.

    Returns:
        str: Matching lines containing the keyword or a not-found message.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()

    matches = [line.strip() for line in lines if keyword.lower() in line.lower()]
    return "\n".join(matches) if matches else "No notes found with that keyword."


@mcp.tool()
def delete_note(index: int) -> str:
    """
    Deletes a specific note by its line number/index.

    Args:
        index (int): The index of the note to delete (0-based).

    Returns:
        str: Confirmation message or error if index is out of range.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()

    if index < 0 or index >= len(lines):
        return "Invalid note index."

    removed = lines.pop(index)
    with open(NOTES_FILE, "w") as f:
        f.writelines(lines)

    return f"Deleted note: {removed.strip()}"


@mcp.tool()
def count_notes() -> int:
    """
    Counts how many notes are currently saved.

    Returns:
        int: The total number of notes.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()

    return len(lines)


@mcp.tool()
def list_notes_with_index() -> str:
    """
    Lists all notes with their index number.

    Returns:
        str: A numbered list of notes or a default message.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()

    if not lines:
        return "No notes available."

    return "\n".join([f"{i}: {line.strip()}" for i, line in enumerate(lines)])


@mcp.tool()
def update_note(index: int, new_content: str) -> str:
    """
    Updates a specific note by index with new content.

    Args:
        index (int): The index of the note to update.
        new_content (str): The new content to replace the old note.

    Returns:
        str: Confirmation message or error if index is out of range.
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()

    if index < 0 or index >= len(lines):
        return "Invalid note index."

    old_note = lines[index].strip()
    lines[index] = new_content + "\n"

    with open(NOTES_FILE, "w") as f:
        f.writelines(lines)

    return f"Note updated from: '{old_note}' to: '{new_content}'"


# Resource is not like a tool rather it's for reading information
# Like getting the most recetn notes


@mcp.resource("notes://latest")
def get_latest_notes() -> str:
    """
    Gets the most recent notes from the sticky notes file.

    Returns:
        str: The last notes entry, If no notes exits, a default message is returned
    """

    ensure_file()
    with open(NOTES_FILE, "r") as f:
        lines = f.readlines()

    return lines[-1].strip() if lines else "No Notes Yet."


@mcp.prompt()
def notes_summary_prompt() -> str:
    """
    Generates a prompt asking AI to summarize all the current notes

    Returns:
        str: A prompt string containing all the notes and ask for the summary
        If no notes exists, a message will be show indicating that
    """
    ensure_file()
    with open(NOTES_FILE, "r") as f:
        contents = f.read().strip()

    if not contents:
        return "There are no notes yet."

    return f"Summarize the current notes: {contents}"
