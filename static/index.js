const slugify = text =>
  text
    .toString()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .trim()
    .replace(/\s+/g, '-')
    .replace(/[^\w-]+/g, '')
    .replace(/--+/g, '-');

const gameIdInput = document.getElementById("gameIdInput");
const startGameButton = document.getElementById("startGameButton");

window.onload = function () {
  gameIdInput.addEventListener("input", function () {
    if (!gameIdInput.value) {
      startGameButton.disabled = true;
    } else {
      startGameButton.disabled = false;
    }
  });

  startGameButton.addEventListener("click", function () {
    const gameId = slugify(gameIdInput.value);
    const uri = `/multiplayer/${gameId}`;
    window.location = uri;
  });
}
