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

const uuidv4 = () => {
  return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
    (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
  );
}

const getElementIndex = (node) => {
  var index = 0;
  while ( (node = node.previousElementSibling) ) {
      index++;
  }
  return index;
}

const createCard = (color, value, hidden = false, draggable = false) => {
  const card = document.createElement('div');

  if (draggable) {
    card.draggable = true;
    card.ondragstart = e => drag(e);
  }  

  card.setAttribute('id', `card_${uuidv4()}`);

  card.style.border = '2px solid black';
  card.style.padding = '5px';
  card.style.display = 'inline-block';
  card.style.fontSize = '0.8rem';
  card.style.width = '20px';
  card.style.height = '35px';
  card.style.borderRadius = '3px';
  card.style.backgroundColor = !hidden ? color.toLowerCase() : 'grey';
  card.innerText = !hidden ? value : '';
  return card;
}

const allowDrop = (ev) => {
  ev.preventDefault();
}

const drag = (e) => {
  e.dataTransfer.setData('index', getElementIndex(e.target));
  e.dataTransfer.setData('id', e.target.id);
}

const drop = (e) => {
  e.preventDefault();
  const index = e.dataTransfer.getData('index');

  console.log(e.target.id);

  if (e.target.id === 'canvas') {
    signal('play_to_canvas', {index: parseInt(index)});
  }
  if (e.target.id === 'palette') {
    signal('play_to_palette', {index: parseInt(index)});
  }
}  

const updateAvailableActions = (msg) => {
  console.log('updateAvailableActions');
}

const updateUI = (msg) => {
  const canvas = getOrCreateElementById('canvas');
  const deck = getOrCreateElementById('deck');
  const hand = getOrCreateElementById('hand');
  const palette = getOrCreateElementById('palette');

  deck.innerHTML = '';
  msg.game.deck.cards.map(card => {
    const cardElement = createCard(card.color, card.value, true);
    deck.appendChild(cardElement);
  });

  if (parseInt(msg.player.id) === parseInt(PLAYER_ID) && msg.game.id == GAME_ID) {
    palette.innerHTML = '';
    msg.player.palette.cards.map(card => {
      const cardElement = createCard(card.color, card.value);
      palette.appendChild(cardElement);
  
      palette.ondrop = e => drop(e);
      palette.ondragover = e => allowDrop(e);
    });
  
    hand.innerHTML = '';
    msg.player.hand.cards.map(card => {
      const cardElement = createCard(card.color, card.value, false, true);
      hand.appendChild(cardElement);
    });
  }

  canvas.innerHTML = '';
  let canvasCard = msg.game.canvas.card;
  const canvasCardElement = createCard(canvasCard.color, canvasCard.value);
  canvas.appendChild(canvasCardElement);

  canvas.ondrop = e => drop(e);
  canvas.ondragover = e => allowDrop(e);
} 

socket.on('state', function(msg) {    
  console.log(msg);
  updateUI(msg);
  updateAvailableActions(msg);
});

window.onload = function() {
  signal('joined');
}
