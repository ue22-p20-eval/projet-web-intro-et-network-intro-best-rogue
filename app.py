from flask import Flask, render_template 
from flask_socketio import SocketIO
from game_backend import Game
from time import time
import json

app = Flask(__name__)
socketio = SocketIO(app)
game = Game()




@app.route("/")
def index():
    map = game.getMap()
    return render_template("index.html", mapdata=map, n_row=len(map), n_col=len(map[0]) )

@socketio.on("move")
def on_move_msg(json, methods=["GET", "POST"]):
    print("received move ws message")
    dx = json['dx']
    dy = json["dy"]

    m1, m2 = game.move(dx,dy)
    data, ret = m1[0], m1[1]
    data2, ret2 = m2[0], m2[1]
    #data2, ret2 = game.moveM()
    if ret:
        socketio.emit("response", data)
    if ret2:
        socketio.emit("responseM", data2)


if __name__=="__main__":
    socketio.run(app, port=5001)