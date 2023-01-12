from threading import Lock
from flask import Flask, session, render_template
from flask_socketio import SocketIO, emit
from core.Game import Game
from time import sleep

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

def get_game_and_player(msg):
  global games
  player_id = int(msg.get('player_id'))
  game_id = msg.get('game_id')
  game = games[game_id]
  player = game.players[player_id]
  return game, player

@socket.on("joined", namespace="/socket")
def joined(msg):
  game, player = get_game_and_player(msg)
  emit("state", {"player": player.serialize(), "game": game.serialize()})
  if len(game.players) == game.number_of_players:
    game.deal_cards()
    sleep(3)
    emit("state", {"player": player.serialize(), "game": game.serialize()}, broadcast=True)    

@socket.on("play_to_canvas", namespace="/socket")
def play_to_canvas(msg):
  game, player = get_game_and_player(msg)
  player.set_card_to_canvas(msg['data']['index'], game.canvas)
  emit("state", {"player": player.serialize(), "game": game.serialize()})

@socket.on("play_to_palette", namespace="/socket")
def play_to_palette(msg):
  game, player = get_game_and_player(msg)
  player.set_card_to_palette(msg['data']['index'])
  emit("state", {"player": player.serialize(), "game": game.serialize()})

