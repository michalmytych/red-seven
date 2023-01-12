const namespace = '/socket';
const socket = io(namespace);

console.log(__playerId);

console.log('HELLO')

const signal = (e, data) => {
  socket.emit(e, {player_id: __playerId, data: data});
}

socket.on('debug', function(msg) {
  console.log(msg)
})

socket.on('player_joined', function(msg) {
  console.log(msg)
})

socket.on('connect', function () {
  console.log('Connected with socket server.')
})

window.onload = function() {
  signal("hello", {counter: 12});
}
