import random as rd
from .player import Player

player = Player(chr(0x1F471))

class Monster:
    def __init__(self, symbol=chr(0x1F470)):
        self._symbol = symbol
        self._x = None
        self._y = None
        self._dx = None
        self._dy = None
        self._life = 2

    def initPos(self, _map, height, width):
        y_init = rd.randint(0, height-1)  
        x_init = rd.randint(0, width-1)
        found = False
        while found is False:
            y_init += 1
            x_init += 1
            for i,c in enumerate(_map[y_init]):
                if c == chr(0x2B1C):
                    x_init = i
                    found = True
                    break
        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol


    def dxdy(self):
        dx, dy = 0, 0
        dx,dy = rd.choice([[0, 1], [0, -1], [1, 0], [-1, 0]])
    
        return dx,dy

    def is_dead(self):
        return self._life <= 0

    def die(self,map):
        map[self._y][self._x] = chr(0x2B1C)
        self._x = None
        self._y = None
    
    def moveM(self,map, players):
        if not self.is_dead():
            dx, dy = self.dxdy()
            new_x = self._x + dx
            new_y = self._y + dy
            
            if map[new_y][new_x] == chr(0x2B1C):
                ret =True
                map[new_y][new_x] = self._symbol
                map[self._y][self._x] = chr(0x2B1C)
                data = [{"i": f"{self._y}", "j":f"{self._x}", "content":chr(0x2B1C)}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol},[dy,dx],self._life]
                self._x = new_x
                self._y = new_y
                self._dx = dx
                self._dy = dy

            elif map[new_y][new_x] == chr(0x1F471):  # Player1
                ret = True
                self._life -= 1
                players[0]._life -= 1
                if not players[0].is_dead():
                    if not self.is_dead():
                        map[new_y][new_x] = chr(0x1F471)
                        map[self._y][self._x] = self._symbol
                        data = [{"i": f"{self._y}", "j":f"{self._x}", "content":self._symbol}, {"i": f"{new_y}", "j":f"{new_x}", "content":chr(0x1F471)}, [0,0], self._life]
                    else :
                        data = [{"i": f"{self._y}", "j":f"{self._x}", "content":chr(0x2B1C)}, {"i": f"{new_y}", "j":f"{new_x}", "content":chr(0x1F471)}, [None,None],0]
                        self.die(map)
                else:
                    #player.game_over()
                    ret = False
                    data = []

            elif map[new_y][new_x] == chr(0x1F990):  # Player2
                ret = True
                self._life -= 1
                players[1]._life -= 1
                if not players[1].is_dead():
                    if not self.is_dead():
                        map[new_y][new_x] = chr(0x1F990)
                        map[self._y][self._x] = self._symbol
                        data = [{"i": f"{self._y}", "j":f"{self._x}", "content":self._symbol}, {"i": f"{new_y}", "j":f"{new_x}", "content":chr(0x1F990)}, [0,0], self._life]
                    else :
                        data = [{"i": f"{self._y}", "j":f"{self._x}", "content":chr(0x2B1C)}, {"i": f"{new_y}", "j":f"{new_x}", "content":chr(0x1F990)}, [None,None],0]
                        self.die(map)
                else:
                    #player.game_over()
                    ret = False
                    data = []
            else:
                ret = False
                data = []
        else :
            ret = False
            data = []
        return data, ret