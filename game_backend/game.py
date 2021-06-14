from .map_generator import Generator
from .player import Player, Baby
from .monsters import Monster
import random as rd


class Game:
    def __init__(self, width=53, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_coins()
        self._generator.gen_potions()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level
        self.height = self._generator.height
        self.width = self._generator.width
        self._players = [Player(chr(0x1F471)), Player(chr(0x1F990))]
        self._initPos_P1 = self._players[0].initPos(self._map)
        self._initPos_P2 = self._players[1].initPos(self._map)
        self.baby = self._generator.gen_baby(self)
        self._Monster = self._generator.gen_monster(self)

    def getMap(self):
        return self._map

    def move(self, dx, dy, i):
        return self._players[i].move(dx, dy, self._map), self._Monster.moveM(self._map, self._players)

    #def moveM(self):
    #    return self._Monster.moveM(self._map, self._player)