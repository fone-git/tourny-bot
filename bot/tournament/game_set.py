from bot.tournament.player import Player


class GameSet:
    # Global counter for game IDs (Reset when rounds is invalidated
    next_id = 1

    def __init__(self, p1: Player, p2: Player, round_):
        self.round_ = round_  # Round that the game is in
        self.game_id = self.new_game_id()
        self.players = [p1, p2]
        self.scores = [0, 0]

        # Stores the game that the winner of this game goes to
        self.next_game = None

        # index of the winner of this game in the next game
        self.next_game_player_ind = None

    def is_won(self):
        for score in self.scores:
            if score > self.round_.best_out_of // 2:
                return True
        return False

    def _is_p_winner(self, score_index: int):
        return ('winner'
                if
                self.round_.best_out_of is not None
                and self.scores[score_index] > self.round_.best_out_of // 2
                else '')

    def is_p1_winner(self):
        return self._is_p_winner(0)

    def is_p2_winner(self):
        return self._is_p_winner(1)

    @property
    def p1(self):
        return self.players[0]

    @property
    def p2(self):
        return self.players[1]

    @property
    def p1_score(self):
        return self.scores[0]

    @property
    def p2_score(self):
        return self.scores[1]

    def __str__(self):
        return f'g{self.game_id}: {self.p1} ({self.p1_score}) ' \
               f'vs {self.p2} ({self.p2_score})'

    def to_player(self) -> Player:
        """
        Creates a player object to represent the unknown winner of this game
        """
        return Player("", f'Winner of Game {self.game_id}', "?")

    @classmethod
    def reset_id_count(cls):
        cls.next_id = 1

    @classmethod
    def new_game_id(cls):
        result = cls.next_id
        cls.next_id += 1
        return result
