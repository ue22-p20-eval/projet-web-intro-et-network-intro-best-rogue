from .map_generator import Generator
from .player import Player
from .monsters import Monster
import random as rd


class Game:
    def __init__(self, width=96, height=32):
        self._generator = Generator(width=width, height=height)
        self._generator.gen_level()
        self._generator.gen_tiles_level()
        self._map = self._generator.tiles_level

        self._player = Player()
        self._player.initPos( self._map )

        #self._Monster = self._generator.gen_monster(self)

    def getMap(self):
        return self._map

    def move(self, dx, dy):
        return self._player.move(dx, dy, self._map)

    def update_Monster(self):
        data_list = []
        for monster in self._Monster:
            data = monster.moveM(self._map)
            data_list.append(data)
        return data_list
        
    def moveM(self, dx = rd.randint(-1,1), dy = rd.randint(-1,1)):
        return self._monster.moveM(dx, dy, self._map)