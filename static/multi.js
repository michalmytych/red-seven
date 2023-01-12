const namespace = '/socket';
const socket = io(namespace);

const signal = (e, data) => {
  socket.emit(e, {
    player_id: PLAYER_ID, 
    game_id: GAME_ID, 
    data: data
  });
}

socket.on('test', function(msg) {
  console.log(msg)
})

window.onload = function() {
  signal("joined");
}
