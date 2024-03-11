# Personalized Letter Generator

This is a simple Python script that generates personalized letters by replacing a placeholder in a template letter with names from a file. This can be useful for generating personalized invitations, thank you letters, or any other form of correspondence.

## Usage

1. **Input Files:**
   - Place the list of names in the `Input/Names/invited_names.txt` file.
   - Place the template letter in the `Input/Letters/starting_letter.txt` file. Ensure that you have a placeholder (`[name]`) where you want the names to be inserted.

2. **Run the Script:**
   - Execute the `personalized_letter_generator.py` script.
   - It will read the names from `invited_names.txt` and the template letter from `starting_letter.txt`.
   - It will then generate personalized letters for each name and save them in the `Output/ReadyToSend/` directory.

3. **Output:**
   - Personalized letters will be saved as individual text files in the `Output/ReadyToSend/` directory.

## Requirements

- Python 3.x

## How it Works

1. Read the list of names from `invited_names.txt`.
2. Read the template letter from `starting_letter.txt`.
3. Iterate through each name, replacing the placeholder `[name]` with the current name.
4. Save each personalized letter to a separate text file in the `Output/ReadyToSend/` directory.

## Example

Suppose `invited_names.txt` contains:
