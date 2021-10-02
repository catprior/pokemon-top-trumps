from main import choose_pokemon

player_name, player_height, player_weight, player_stat, \
    player_id, player_image, player_primary, player_secondary, player_tcg_icon = choose_pokemon(25)


def test_api_request_name():
    assert player_name == 'Pikachu'


def test_api_request_height():
    assert player_height == 4


def test_api_request_weight():
    assert player_weight == 60


def test_api_request_stat():
    assert player_stat == 35


def test_api_request_id():
    assert player_id == 25


def test_api_request_image():
    assert player_image == 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/' \
                           'pokemon/other/official-artwork/25.png'


def test_card_styles_primary():
    assert player_primary == 'yellow'


def test_card_styles_secondary():
    assert player_secondary == 'orange'


def test_card_styles_tcg_icon():
    assert player_tcg_icon == '/static/electric_icon.png'
