// Scroll to top on button click
var btn = document.getElementById('scrollToTopBtn');
btn.addEventListener('click', () => window.scrollTo({
  top: 0,
  behavior: 'smooth',
}));
