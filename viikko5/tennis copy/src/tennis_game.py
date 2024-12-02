class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self._equal_score()
        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self._advantage_or_win()
        else:
            return self._regular_score()

    def _equal_score(self):
        scores = ["Love-All", "Fifteen-All", "Thirty-All", "Deuce"]
        return scores[self.m_score1] if self.m_score1 < 3 else "Deuce"

    def _advantage_or_win(self):
        minus_result = self.m_score1 - self.m_score2
        if minus_result == 1:
            return "Advantage " + self.player1_name
        elif minus_result == -1:
            return "Advantage " + self.player2_name
        elif minus_result >= 2:
            return "Win for " + self.player1_name
        else:
            return "Win for " + self.player2_name

    def _regular_score(self):
        score_names = ["Love", "Fifteen", "Thirty", "Forty"]
        return f"{score_names[self.m_score1]}-{score_names[self.m_score2]}"
