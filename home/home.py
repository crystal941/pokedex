from flask import Blueprint, render_template, request

from home.services import fetch_pokemon_data

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/')
def home():
    return render_template('index.html')


@home_blueprint.route('/pokemons', methods=['GET'])
def browse_pokemons():
    page = int(request.args.get('page', 1))
    sort = request.args.get('sort', 'id')  # Default sort by ID
    order = request.args.get('order', 'asc')  # Default order ascending

    pokemon_data, total_pages = fetch_pokemon_data(page)

    # Sort the data based on the query parameters
    if sort in ['height', 'weight']:
        pokemon_data = sorted(pokemon_data, key=lambda x: x[sort], reverse=(order == 'desc'))
    elif sort == 'type':
        pokemon_data = sorted(pokemon_data, key=lambda x: x['types'][0] if x['types'] else '', reverse=(order == 'desc'))
    elif sort == 'id':
        pokemon_data = sorted(pokemon_data, key=lambda x: x['id'], reverse=(order == 'desc'))
    elif sort == 'name':
        pokemon_data = sorted(pokemon_data, key=lambda x: x['name'].lower(), reverse=(order == 'desc'))

    return render_template('pokemonList.html', pokemon_data=pokemon_data, total_pages=total_pages,
                           page=page, sort=sort, order=order)
