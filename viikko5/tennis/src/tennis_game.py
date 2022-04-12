class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def uneven_score_win_situation(self, player1_score, player2_score):
        current_score_situation = player1_score - player2_score
        if current_score_situation == 1:
            score = "Advantage player1"
        elif current_score_situation == -1:
            score = "Advantage player2"
        elif current_score_situation >=2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def scores_to_string(self, player_score):
        if player_score == 0:
            score_string = "Love"
        elif player_score == 1:
            score_string = "Fifteen"
        elif player_score == 2:
            score_string = "Thirty"
        elif player_score == 3:
            score_string = "Forty"
        return score_string

    def get_score(self):
        if self.player1_score == self.player2_score:
            if self.player1_score <= 3:
                score = self.scores_to_string(self.player1_score) + "-All"
            else:
                score = "Deuce"
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.uneven_score_win_situation(self.player1_score, self.player2_score)
        else:
            score = self.scores_to_string(self.player1_score) + "-" + self.scores_to_string(self.player2_score)

        return score
