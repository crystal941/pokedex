"""
In-memory cache for storing Pokemon data.
Minimising the time to repeatedly requesting from endpoints.
"""

pokemon_cache = {}


def get_cache(offset):
    """
    Retrieves cached Pokemon data by provided offset.
    """
    return pokemon_cache.get(offset)


def set_cache(offset, data):
    """
    Caches Pokemon data using offset.
    """
    pokemon_cache[offset] = data


def get_cached_pokemon(id_or_name):
    """
    Retrieves a cached Pokémon by ID or name.
    """
    return pokemon_cache.get(id_or_name)


def set_cached_pokemon(id_or_name, pokemon_data):
    """
    Caches a Pokémon's data using its ID or name as the key.
    """
    pokemon_cache[id_or_name] = pokemon_data
