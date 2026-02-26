console.log("recentie.js geopend")

const track = document.querySelector('.track');
const items = document.querySelectorAll('.item');

const slideWidth = 500;
const originalCount = items.length / 2; // omdat we dupliceren
let index = 0;

function moveSlide() {
  index++;
  track.style.transition = "transform 0.8s ease-in-out";
  track.style.transform = `translateX(-${index * slideWidth}px)`;

  // Zodra we bij de kopie zijn, resetten zonder animatie
  if (index === originalCount) {
    setTimeout(() => {
      track.style.transition = "none";
      track.style.transform = `translateX(0px)`;
      index = 0;
    }, 5000);
  }
}

setInterval(moveSlide, 3000);