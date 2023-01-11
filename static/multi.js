const namespace = '/sockets';
const socket = io(namespace);

console.log('HELLO')

socket.on('debug', function(msg) {
  console.log(msg)
})

socket.on('connect', function () {
  console.log('Connected with socket server.')
})
