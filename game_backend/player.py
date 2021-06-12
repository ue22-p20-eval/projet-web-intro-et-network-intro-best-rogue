class Player:
    def __init__(self, symbol="@"):
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
                if c == ".":
                    x_init = i
                    found = True
                    break

        self._x = x_init
        self._y = y_init

        _map[self._y][self._x] = self._symbol


    def move(self, dx, dy, map):
        new_x = self._x + dx
        new_y = self._y + dy

        if map[new_y][new_x] == "." :
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self._money, self._life]
            self._x = new_x
            self._y = new_y
        elif map[new_y][new_x] == "$" :
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            self._money += 1
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self._money, self._life]
            self._x = new_x
            self._y = new_y
            
        elif map[new_y][new_x] == "M" :
            ret = True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            self._life -= 1
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol}, self._money, self._life]
            
        else:
            ret = False
            data = []
        return data, ret