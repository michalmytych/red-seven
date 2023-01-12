const namespace = '/socket';
const socket = io(namespace);

const signal = (e, data) => {
  socket.emit(e, {
    player_id: PLAYER_ID, 
    game_id: GAME_ID, 
    data: data
  });
}

const getOrCreateElementById = (id) => {
  let element = document.getElementById(id)
  if (!element) {
    element = document.createElement('div')
    element.id = id
    document.body.appendChild(element)
  }
  return element
}

const createCard = (color, value, hidden = false) => {
  const card = document.createElement('div')
  card.display = 'inline-block'
  card.style.fontSize = '0.8rem'
  card.style.width = '20px'
  card.style.height = '35px'
  card.style.borderRadius = '3px'
  card.style.backgroundColor = !hidden ? color.toLowerCase() : 'grey'
  card.innerText = !hidden ? value : ''
  return card
}

const updateUI = (msg) => {
  const canvas = getOrCreateElementById('canvas')
  const deck = getOrCreateElementById('deck')
  const hand = getOrCreateElementById('hand')
  const palette = getOrCreateElementById('palette')

  deck.innerHTML = ''
  msg.game.deck.cards.map(card => {
    const cardElement = createCard(card.color, card.value) // hidden = true
    deck.appendChild(cardElement)
  })

  palette.innerHTML = ''
  msg.player.palette.cards.map(card => {
    const cardElement = createCard(card.color, card.value)
    palette.appendChild(cardElement)
  })

  hand.innerHTML = ''
  msg.player.hand.cards.map(card => {
    const cardElement = createCard(card.color, card.value)
    hand.appendChild(cardElement)
  })

  canvas.innerHTML = ''
  let canvasCard = msg.game.canvas.card
  const canvasCardElement = createCard(canvasCard.color, canvasCard.value)
  canvas.appendChild(canvasCardElement)
} 

socket.on('test', function(msg) {
  updateUI(msg)
  console.log(msg);
})

window.onload = function() {
  signal("joined");
}
