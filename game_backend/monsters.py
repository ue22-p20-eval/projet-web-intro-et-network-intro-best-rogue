import random as rd

class Monster:
    def __init__(self, symbol="M"):
        self._symbol = symbol
        self._x = None
        self._y = None
        self._dx = None
        self._dy = None
        self._life = 3

    def initPos(self, _map, height, width):
        y_init = rd.randint(0, height-1)  
        x_init = rd.randint(0, width-1)
        found = False
        while found is False:
            y_init += 1
            x_init +=1
            for i,c in enumerate(_map[y_init]):
                if c == ".":
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
    
    def moveM(self,map):
        dx, dy = self.dxdy()
        new_x = self._x + dx
        new_y = self._y + dy
        
        if map[new_y][new_x] == ".":
            ret =True
            map[new_y][new_x] = self._symbol
            map[self._y][self._x] = "."
            data = [{"i": f"{self._y}", "j":f"{self._x}", "content":"."}, {"i": f"{new_y}", "j":f"{new_x}", "content":self._symbol},[dy,dx]]
            self._x = new_x
            self._y = new_y
            self._dx = dx
            self._dy = dy
 
        else:
            ret = False
            data = []
        return data, ret