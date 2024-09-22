from flask import Blueprint, render_template, request
from browse.services import fetch_pokemon_details

browse_blueprint = Blueprint('browse_bp', __name__)


@browse_blueprint.route('/pokemon/<id_or_name>', methods=['GET'])
def pokemon_detail(id_or_name):
    """
    Fetches and displays details for a specific Pokémon.
    """
    try:
        pokemon = fetch_pokemon_details(id_or_name)
        return render_template('pokemonDetail.html', pokemon=pokemon)
    except Exception as e:
        return str(e), 404
