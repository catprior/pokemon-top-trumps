from flask import Flask, render_template, session
import random
import requests
from pkmn_types import get_pkmn_style
import json

app = Flask(__name__)

app.config.from_file('config.json', load=json.load)

# Config Variables
app.secret_key = app.config["APP.SECRET_KEY"]
api_url = app.config["TEXT_API_URL"]
image_api_url = app.config["IMAGE_API_URL"]
max_pkmn_no = int(app.config["MAX_PKMN_NO"])


# Get random Pokemon ID no
def get_pkmn_id():
    pokemon_no = random.randint(1, max_pkmn_no)
    return pokemon_no


# API request
def choose_pokemon(pokemon_no):
    player_url = api_url.format(pokemon_no)
    player_response = requests.get(player_url)
    player_pokemon = player_response.json()

    player_name = player_pokemon['name'].title()
    player_height = player_pokemon['height']
    player_weight = player_pokemon['weight']
    player_type = player_pokemon['types'][0]['type']['name']
    player_stat = player_pokemon['stats'][0]['base_stat']
    player_id = player_pokemon['id']
    player_image = image_api_url.format(pokemon_no)

    player_primary = get_pkmn_style(player_type)[0]
    player_secondary = get_pkmn_style(player_type)[1]
    player_tcg_icon = get_pkmn_style(player_type)[2]

    return player_name, player_height, player_weight, player_stat,\
        player_id, player_image, player_primary, player_secondary, player_tcg_icon


# App start page
@app.route('/')
def index():
    return render_template('index.html')


# Start game - Player One (Opponent) chooses Pokemon
@app.route("/submit/", methods=['POST'])
def start_game():
    # Get Pokemon from API
    p1_no = get_pkmn_id()
    p1_name, p1_height, p1_weight, p1_stat, p1_id, p1_image, p1_primary,\
        p1_secondary, p1_tcg_icon = choose_pokemon(p1_no)

    # Add Player One's (Opponent) Pokemon from to session variables to carry them across pages
    session["p1_name"] = p1_name
    session["p1_height"] = p1_height
    session["p1_weight"] = p1_weight
    session["p1_stat"] = p1_stat
    session["p1_id"] = p1_id
    session["p1_primary"] = p1_primary
    session["p1_secondary"] = p1_secondary
    session["p1_tcg_icon"] = p1_tcg_icon
    session["p1_image"] = p1_image

    return render_template('opponents-turn.html',
                           p1_name=p1_name,
                           p1_weight=p1_weight,
                           p1_height=p1_height,
                           p1_image=p1_image,
                           p1_stat=p1_stat,
                           p1_id=p1_id,
                           p1_primary=p1_primary,
                           p1_secondary=p1_secondary,
                           p1_tcg_icon=p1_tcg_icon)


# Player's turn - chooses stat "weight"
@app.route("/submit/weight/", methods=['POST'])
def weight_game():
    # Get Player Two's Pokemon from API
    p2_no = get_pkmn_id()
    p2_name, p2_height, p2_weight, p2_stat, p2_id, p2_image, p2_primary,\
        p2_secondary, p2_tcg_icon = choose_pokemon(p2_no)

    # Get Player One's (Opponent) Pokemon from previous page
    p1_name = session.get("p1_name", None)
    p1_height = session.get("p1_height", None)
    p1_weight = session.get("p1_weight", None)
    p1_stat = session.get("p1_stat", None)
    p1_id = session.get("p1_id", None)
    p1_primary = session.get("p1_primary", None)
    p1_secondary = session.get("p1_secondary", None)
    p1_tcg_icon = session.get("p1_tcg_icon", None)
    p1_image = session.get("p1_image", None)

    # Compare stats to see who wins!
    if p1_weight == p2_weight:
        message = "Your {} and {} are the same weight.".format(p2_name, p1_name)
        result = "It's a Tie!"
        alert = "warning"
    elif p2_weight > p1_weight:
        message = "Your {} is heavier than {}.".format(p2_name, p1_name)
        result = "You Win!"
        alert = "success"
    else:
        message = "{} is heavier than your {}.".format(p1_name, p2_name)
        result = "You Lose!"
        alert = "danger"

    return render_template('players-turn.html', p2_name=p2_name,
                           p2_weight=p2_weight,
                           p2_height=p2_height,
                           p2_image=p2_image,
                           p2_stat=p2_stat,
                           p2_id=p2_id,
                           p2_primary=p2_primary,
                           p2_secondary=p2_secondary,
                           p2_tcg_icon=p2_tcg_icon,
                           p1_name=p1_name,
                           p1_weight=p1_weight,
                           p1_height=p1_height,
                           p1_image=p1_image,
                           p1_id=p1_id,
                           p1_stat=p1_stat,
                           p1_primary=p1_primary,
                           p1_secondary=p1_secondary,
                           p1_tcg_icon=p1_tcg_icon,
                           result=result,
                           alert=alert,
                           message=message)


# Player's turn - chooses stat "height"
@app.route("/submit/height/", methods=['POST'])
def height_game():
    # Get Player Two's Pokemon from API
    p2_no = get_pkmn_id()
    p2_name, p2_height, p2_weight, p2_stat, p2_id, p2_image, p2_primary,\
        p2_secondary, p2_tcg_icon = choose_pokemon(p2_no)

    # Get Player One's (Opponent) Pokemon from previous page
    p1_name = session.get("p1_name", None)
    p1_height = session.get("p1_height", None)
    p1_weight = session.get("p1_weight", None)
    p1_stat = session.get("p1_stat", None)
    p1_id = session.get("p1_id", None)
    p1_primary = session.get("p1_primary", None)
    p1_secondary = session.get("p1_secondary", None)
    p1_tcg_icon = session.get("p1_tcg_icon", None)
    p1_image = session.get("p1_image", None)

    # Compare stats to see who wins!
    if p1_height == p2_height:
        message = "Your {} and {} are the same height.".format(p2_name, p1_name)
        result = "It's a Tie!"
        alert = "warning"
    elif p2_height > p1_height:
        message = "Your {} is taller than {}.".format(p2_name, p1_name)
        result = "You Win!"
        alert = "success"
    else:
        message = "{} is taller than your {}.".format(p1_name, p2_name)
        result = "You Lose!"
        alert = "danger"

    return render_template('players-turn.html', p2_name=p2_name,
                           p2_weight=p2_weight,
                           p2_height=p2_height,
                           p2_image=p2_image,
                           p2_stat=p2_stat,
                           p2_id=p2_id,
                           p2_primary=p2_primary,
                           p2_secondary=p2_secondary,
                           p2_tcg_icon=p2_tcg_icon,
                           p1_name=p1_name,
                           p1_weight=p1_weight,
                           p1_height=p1_height,
                           p1_image=p1_image,
                           p1_id=p1_id,
                           p1_stat=p1_stat,
                           p1_primary=p1_primary,
                           p1_secondary=p1_secondary,
                           p1_tcg_icon=p1_tcg_icon,
                           result=result,
                           alert=alert,
                           message=message)


# Player's turn - chooses stat "id"
@app.route("/submit/id/", methods=['POST'])
def id_game():
    # Get Player Two's Pokemon from API
    p2_no = get_pkmn_id()
    p2_name, p2_height, p2_weight, p2_stat, p2_id, p2_image, p2_primary,\
        p2_secondary, p2_tcg_icon = choose_pokemon(p2_no)

    # Get Player One's (Opponent) Pokemon from previous page
    p1_name = session.get("p1_name", None)
    p1_height = session.get("p1_height", None)
    p1_weight = session.get("p1_weight", None)
    p1_stat = session.get("p1_stat", None)
    p1_id = session.get("p1_id", None)
    p1_primary = session.get("p1_primary", None)
    p1_secondary = session.get("p1_secondary", None)
    p1_tcg_icon = session.get("p1_tcg_icon", None)
    p1_image = session.get("p1_image", None)

    # Compare stats to see who wins!
    if p1_id == p2_id:
        message = "Your {} and {} have the same id.".format(p2_name, p1_name)
        result = "It's a Tie!"
        alert = "warning"
    elif p2_id > p1_id:
        message = "Your {} has a higher id than {}.".format(p2_name, p1_name)
        result = "You Win!"
        alert = "success"
    else:
        message = "{} has a higher id than your {}.".format(p1_name, p2_name)
        result = "You Lose!"
        alert = "danger"

    return render_template('players-turn.html', p2_name=p2_name,
                           p2_weight=p2_weight,
                           p2_height=p2_height,
                           p2_image=p2_image,
                           p2_stat=p2_stat,
                           p2_id=p2_id,
                           p2_primary=p2_primary,
                           p2_secondary=p2_secondary,
                           p2_tcg_icon=p2_tcg_icon,
                           p1_name=p1_name,
                           p1_weight=p1_weight,
                           p1_height=p1_height,
                           p1_image=p1_image,
                           p1_id=p1_id,
                           p1_stat=p1_stat,
                           p1_primary=p1_primary,
                           p1_secondary=p1_secondary,
                           p1_tcg_icon=p1_tcg_icon,
                           result=result,
                           alert=alert,
                           message=message)


# Player's turn - chooses stat "base stat"
@app.route("/submit/stat/", methods=['POST'])
def stat_game():
    # Get Player Two's Pokemon from API
    p2_no = get_pkmn_id()
    p2_name, p2_height, p2_weight, p2_stat, p2_id, p2_image, p2_primary,\
        p2_secondary, p2_tcg_icon = choose_pokemon(p2_no)

    # Get Player One's (Opponent) Pokemon from previous page
    p1_name = session.get("p1_name", None)
    p1_height = session.get("p1_height", None)
    p1_weight = session.get("p1_weight", None)
    p1_stat = session.get("p1_stat", None)
    p1_id = session.get("p1_id", None)
    p1_primary = session.get("p1_primary", None)
    p1_secondary = session.get("p1_secondary", None)
    p1_tcg_icon = session.get("p1_tcg_icon", None)
    p1_image = session.get("p1_image", None)

    # Compare stats to see who wins!
    if p1_stat == p2_stat:
        message = "Your {} and {} have the same base stat.".format(p2_name, p1_name)
        result = "It's a Tie!"
        alert = "warning"
    elif p2_stat > p1_stat:
        message = "Your {} has a higher base stat than {}.".format(p2_name, p1_name)
        result = "You Win!"
        alert = "success"
    else:
        message = "{} has a higher base stat than your {}.".format(p1_name, p2_name)
        result = "You Lose!"
        alert = "danger"

    return render_template('players-turn.html', p2_name=p2_name,
                           p2_weight=p2_weight,
                           p2_height=p2_height,
                           p2_image=p2_image,
                           p2_stat=p2_stat,
                           p2_id=p2_id,
                           p2_primary=p2_primary,
                           p2_secondary=p2_secondary,
                           p2_tcg_icon=p2_tcg_icon,
                           p1_name=p1_name,
                           p1_weight=p1_weight,
                           p1_height=p1_height,
                           p1_image=p1_image,
                           p1_id=p1_id,
                           p1_stat=p1_stat,
                           p1_primary=p1_primary,
                           p1_secondary=p1_secondary,
                           p1_tcg_icon=p1_tcg_icon,
                           result=result,
                           alert=alert,
                           message=message)


if __name__ == '__main__':
    app.run()
