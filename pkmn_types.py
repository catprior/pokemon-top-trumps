def get_pkmn_style(type):
    if type == 'grass':
        primary = 'yellow'
        secondary = 'green'
        tcg_icon = '/static/grass_icon.png'
    elif type == 'fire':
        primary = 'orange'
        secondary = 'red'
        tcg_icon = '/static/fire_icon.png'
    elif type == 'water':
        primary = 'deepskyblue'
        secondary = 'cadetblue'
        tcg_icon = '/static/water_icon.png'
    elif type == 'bug':
        primary = 'yellow'
        secondary = 'green'
        tcg_icon = '/static/bug_icon.png'
    elif type == 'normal':
        primary = 'silver'
        secondary = 'slategrey'
        tcg_icon = '/static/normal_icon.png'
    elif type == 'poison':
        primary = 'fuchsia'
        secondary = 'purple'
        tcg_icon = '/static/poison_icon.png'
    elif type == 'electric':
        primary = 'yellow'
        secondary = 'orange'
        tcg_icon = '/static/electric_icon.png'
    elif type == 'ground':
        primary = 'orange'
        secondary = 'brown'
        tcg_icon = '/static/ground_icon.png'
    elif type == 'fairy':
        primary = 'pink'
        secondary = 'palevioletred'
        tcg_icon = '/static/fairy_icon.png'
    elif type == 'fighting':
        primary = 'orange'
        secondary = 'brown'
        tcg_icon = '/static/fighting_icon.png'
    elif type == 'psychic':
        primary = 'fuchsia'
        secondary = 'purple'
        tcg_icon = '/static/psychic_icon.png'
    elif type == 'rock':
        primary = 'orange'
        secondary = 'brown'
        tcg_icon = '/static/rock_icon.png'
    elif type == 'ghost':
        primary = 'mediumslateblue'
        secondary = 'darkslateblue'
        tcg_icon = '/static/ghost_icon.png'
    elif type == 'ice':
        primary = 'powderblue'
        secondary = 'turquoise'
        tcg_icon = '/static/ice_icon.png'
    elif type == 'dragon':
        primary = 'mediumslateblue'
        secondary = 'darkslateblue'
        tcg_icon = '/static/dragon_icon.png'
    else:
        primary = 'grey'
        secondary = 'grey'
        tcg_icon = '/static/pokeball-icon.png'
    return primary, secondary, tcg_icon
