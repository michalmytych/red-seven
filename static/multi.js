const namespace = '/socket';
const socket = io(namespace);

const signal = (e, data) => {
  socket.emit(e, {player_id: __playerId, data: data});
}

socket.on('test', function(msg) {
  console.log(msg)
})

window.onload = function() {
  signal("hello", {counter: 12});
}
