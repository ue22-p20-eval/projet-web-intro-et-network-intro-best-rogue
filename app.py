from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game
from time import time
import json

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()

global move_time
move_time = time()



@app.route("/")
def index():
    map = game.getMap()
    return render_template("index.html", mapdata=map, n_row=len(map), n_col=len(map[0]) )

@socketio.on("move")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]

    data, ret = game.move(dx,dy)
    if ret:
        socketio.emit("response", data)

@socketio.on("monster_move")
def monster_move():
    global move_time
    if time()-move_time > 0.2:
        move_time = time()
        data_list = game.update_Monster()
        N = len(data_list)
        socketio.emit("monster_response", json.dumps([N, data_list]))



if __name__=="__main__":
    socketio.run(app, port=5001)