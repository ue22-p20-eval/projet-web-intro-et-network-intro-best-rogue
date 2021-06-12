
class Player:
    def __init__(self, symbol=chr(0x1F471)):
        self._symbol = symbol
        self._x = None
        self._y = None
        self._money = 0
        self._life = 3

    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_init = n_row//2
        found = False
        while found is False:
            y_init += 1
            for i,c in enumerate(_map[y_init]):
                if c == chr(0x2B1C):
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol
    
    def is_dead(self):
        return self._life <= 0

    #def game_over(self):
    #    return None

    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy
        #print(self._life)

        if map[new_y][new_x] == chr(0x2B1C) :
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = chr(0x2B1C)
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":chr(0x2B1C)}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self._money, self._life]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == chr(0x1F4A8) :
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = chr(0x2B1C)
            self._money += 1
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":chr(0x2B1C)}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self._money, self._life]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == chr(0x1F476) :
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = chr(0x2B1C)
            self._life += 1
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":chr(0x2B1C)}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self._money, self._life]
            self._x = new_x
            self._y = new_y

        elif map[new_y][new_x] == chr(0x1F470):
            ret = True
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":self._symbol}, {"i": f"{new_y}", "j":f"{new_x}", "content":chr(0x1F470)}, self._money, self._life]

        else:
            ret = False
            data = []
        return data, ret

class Cake:
    def __init__(self, symbol="C"):
        self._symbol = symbol
        self._x = None
        self._y = None


    def initPos(self, _map):
        n_row = len(_map)
        #n_col = len(_map[0])

        y_init = 3*n_row//4
        found = False
        while found is False:
            y_init -= 1
            for i,c in enumerate(_map[y_init]):
                if c == chr(0x2B1C):
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol