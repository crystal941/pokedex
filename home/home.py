from flask import Blueprint, render_template, request

from home.services import fetch_pokemon_data

home_blueprint = Blueprint('home_bp', __name__)


@home_blueprint.route('/')
def home():
    return render_template('index.html')


