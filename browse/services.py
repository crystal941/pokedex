import requests

from adapters.memory_repository import get_cached_pokemon, set_cached_pokemon


def fetch_pokemon_details(id_or_name):
    """
    Fetches a single Pokémon's data by ID or name.
    First checks the cache; if not found, fetches from PokeAPI and caches it.
    """
    # Check if the Pokémon is already cached
    cached_pokemon = get_cached_pokemon(id_or_name)
    if cached_pokemon:
        return cached_pokemon

    # If not in cache, fetch from the API
    api_url = f"https://pokeapi.co/api/v2/pokemon/{id_or_name}"
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        # Cache the Pokémon data
        set_cached_pokemon(id_or_name, pokemon_data)
        return pokemon_data
    else:
        raise Exception(f"Failed to fetch data for Pokémon {id_or_name}. Status code: {response.status_code}")
