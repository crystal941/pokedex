import requests

from adapters.memory_repository import get_cache, set_cache

# Set up constants for pagination
TOTAL_POKEMON = 151
POKEMON_PER_PAGE = 8


def unpack_data(data):
    # Unpack only the required fields for rendering
    detail = []
    for pokemon in data:
        detail.append({
            'id': pokemon['id'],
            'name': pokemon['name'],
            'types': [t['type']['name'] for t in pokemon['types']],
            'height': pokemon['height'],
            'weight': pokemon['weight']
        })
    return detail


def fetch_pokemon_data(page=1):
    # Calculate the offset based on the page
    offset = (page - 1) * POKEMON_PER_PAGE
    total_pages = (TOTAL_POKEMON + POKEMON_PER_PAGE - 1) // POKEMON_PER_PAGE

    # Make sure not exceed limit
    if offset + POKEMON_PER_PAGE > TOTAL_POKEMON:
        limit = TOTAL_POKEMON - offset
    else:
        limit = POKEMON_PER_PAGE

    # Check if data is cached for the current offset
    cached_data = get_cache(offset)
    if cached_data:
        # Unpack only the required fields for rendering
        pokemon_details = unpack_data(cached_data)
        return pokemon_details, total_pages

    # Fetch data from the API with limit and offset
    url = f"https://pokeapi.co/api/v2/pokemon?limit={limit}&offset={offset}"
    response = requests.get(url)
    pokemon_list = response.json().get('results', [])

    # Fetch details for each Pokémon
    pokemon_data = []
    for pokemon in pokemon_list:
        details_url = pokemon['url']
        details_response = requests.get(details_url)
        details_data = details_response.json()
        pokemon_data.append(details_data)

    # Store the fetched data in cache
    set_cache(offset, pokemon_data)

    pokemon_details = unpack_data(pokemon_data)
    return pokemon_details, total_pages
