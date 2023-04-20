var spinner = document.querySelector('.spinner');
var degree = 0;
 function animate() {
  degree += 15;
  if (degree > 360) {
    degree = 0;
  }
  spinner.style.transform = 'rotate(' + degree + 'deg)';
  requestAnimationFrame(animate);
}
 animate();