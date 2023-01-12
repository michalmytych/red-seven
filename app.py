from threading import Lock
from flask import Flask, session, render_template
from flask_socketio import SocketIO, emit
from core.Game import Game

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET'

socket = SocketIO(
    app, 
    logger=True, 
    async_mode=None,
    engineio_logger=True
)

thread = None
thread_lock = Lock()
games = {}

@app.route("/")
def index():
    return render_template('index.html', sync_mode=socket.async_mode)


@app.route("/multiplayer/<game_id>")
def multiplayer(game_id):
    global games
    game = games.get(game_id)
    if not game:
      game = Game(2, game_id)
      games[game_id] = game  
    player = game.assign_player()
    if not player:
      return render_template('game-busy.html')
    return render_template('multi.html', game=game, player=player)


@socket.on("hello", namespace="/socket")
def hello(msg):
  print(msg)
