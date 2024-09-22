# Pokédex App

A simple Flask application that fetches and displays Pokémon data from the [PokéAPI](https://pokeapi.co). 

This app showcases a list of the original 151 Pokémons, caching the data for efficient loading and rendering on the webpage.

## Features

- **Pokémon Data Fetching**: Retrieves data from the PokéAPI.
- **Caching**: Stores fetched Pokémon data in memory for quick access.
- **Pagination**: Displays Pokémon data in pages, with 8 Pokémon per page for better usability.
- **Sorting**: Sorts the Pokémon data by ID, Name, Type, Height, and Weight in ascending and descending orders.

## Technologies Used

- **Python**: The backend language for the Flask application.
- **Flask**: The web framework used to build the app.
- **Requests**: For making API calls to the PokéAPI.
- **HTML/CSS**: For frontend rendering.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/crystal941/pokedex.git
2. Create a virtual environment:

   **MacOS**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
   **Windows**
   ```bash
   py -3 -m venv venv
   venv\Scripts\activate
4. Install the required packages:
   ```bash
   pip install -r requirements.txt

## Usage

1. Start the Flask development server:
   ```bash
   flask run
   ```

2. Open your browser and go to `http://127.0.0.1:5000` to view the Pokédex app.

## Developer's Note

I had fun developing this little app! It’s been a great way to dive into the world of Pokémon and web development. 

I look forward to adding more features in the future, so stay tuned for updates! Gotta catch 'em all!✨


