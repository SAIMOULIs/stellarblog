function toggleDarkMode() {
  document.body.classList.toggle('dark-mode');
  let cards = document.getElementsByClassName('glass');
  for (let i = 0; i < cards.length; i++) {
    cards[i].classList.toggle('glass-dark');
  }
}
