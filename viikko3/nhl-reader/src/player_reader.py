import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url
        self._response = requests.get(url).json()

    def get_players(self):
        players = []
        #print(self._response)
        for player_dict in self._response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            players.append(player)
        return players