class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
        self._players = self._reader.get_players()

    def top_scorers_by_nationality(self, nat):
        players_nat = [x for x in self._players if x.nationality == nat]
        players_nat.sort(key=lambda x: x.total_points, reverse=True)
        return players_nat
