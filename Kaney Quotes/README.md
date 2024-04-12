# Kanye Says...

This simple Python application displays a Kanye West quote each time you click on the Kanye image.

## Requirements

To run this application, you need to have Python installed on your system. Additionally, make sure to install the `requests` library. You can install it via pip:


## How to Run

1. Clone this repository to your local machine.
2. Navigate to the directory where you cloned the repository.
3. Make sure you have the necessary images (`background.png` and `kanye.png`) in the `Kaney Quotes` directory.
4. Run the Python script `kanye_quotes.py`.


5. Click on the image of Kanye West to fetch a new quote.

## Code Explanation

- The application is built using Python's Tkinter library for the graphical user interface (GUI).
- It imports the necessary modules: `Tkinter` and `requests`.
- `get_quote()` function sends a GET request to the "https://api.kanye.rest" API to fetch a Kanye West quote. It then updates the text displayed on the canvas with the fetched quote.
- The GUI is created with a canvas widget to display the background image and the quote text. The quote text is initially set to "Kanye Quote Goes HERE".
- The Kanye image is added as a button, and when clicked, it calls the `get_quote()` function to fetch and display a new quote.
- The application window is created using `Tk()`, with title "Kanye Says..." and padding of 50 pixels.
- The window is structured with the canvas widget in the first row and the Kanye button in the second row.

## Additional Notes

- Make sure you have an active internet connection to fetch quotes from the API.
- This is a simple example of how to fetch data from an API and display it in a Tkinter application. You can extend it by adding error handling, more features, or integrating with other APIs.
