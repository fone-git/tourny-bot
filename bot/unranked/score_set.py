from dataclasses import dataclass, field
from typing import Set, Union

from bot.common.player import Player


@dataclass
class ScoreSet:
    score: int
    players: Set[Player] = field(default_factory=set)
    _str_disp: Union[str, None] = None

    def add(self, player: Player):
        """
        Adds the player if there were not already there otherwise does nothing
        :param player: The player to be added
        """
        self.players.add(player)
        self.invalidate_calculated()

    def remove(self, player: Player):
        """
        Removes the player passed (or does nothing)
        :param player: Player to be removed
        """
        self.players.remove(player)
        self.invalidate_calculated()

    def has_players(self):
        return len(self.players) > 0

    def invalidate_calculated(self):
        self._str_disp = None

    def __str__(self):
        if self._str_disp is None:
            self._str_disp = f'{self.score} - {self.players_as_str()}'
        return self._str_disp

    def players_as_str(self):
        result = ""
        for player in self.players:
            result += f'{player}, '
        if result != "":
            # Crop of trailing ", "
            result = result[:-2]

        return result
