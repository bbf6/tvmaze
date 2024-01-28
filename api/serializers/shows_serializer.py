def get_channel(show):
    if show['show']['webChannel'] is None:
        return show['show']['network']['name']
    return show['show']['webChannel']['name']

def search_item_format(show) -> dict:
    return {
      'id': show['show']['id'],
      'name': show['show']['name'],
      'channel': get_channel(show),
      'summary': show['show']['summary'],
      'genres': show['show']['genres']
    }

def search_format(shows) -> list:
    return list(map(search_item_format, shows))
