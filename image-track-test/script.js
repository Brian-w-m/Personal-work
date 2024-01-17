const track = document.getElementById("image-track");

const handleOnDown = e => track.dataset.mouseDownAt = e.clientX;

const handleOnUp = () => {
  track.dataset.mouseDownAt = "0";  
  track.dataset.prevPercentage = track.dataset.percentage;
}

const handleOnMove = e => {
  if(track.dataset.mouseDownAt === "0") return;
  
  const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
        maxDelta = window.innerWidth / 2;
  
  const percentage = (mouseDelta / maxDelta) * -100,
        nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
        nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);
  
  track.dataset.percentage = nextPercentage;
  
  track.animate({
    transform: `translate(${nextPercentage}%, -50%)`
  }, { duration: 1200, fill: "forwards" });
  
  for(const image of track.getElementsByClassName("image")) {
    image.animate({
      objectPosition: `${100 + nextPercentage}% center`
    }, { duration: 1200, fill: "forwards" });
  }
  document.getElementById("img-perc").textContent = Math.round((-nextPercentage/100)*8);
}


/* -- Had to add extra lines for touch events -- */

window.onmousedown = e => handleOnDown(e);

window.ontouchstart = e => handleOnDown(e.touches[0]);

window.onmouseup = e => handleOnUp(e);

window.ontouchend = e => handleOnUp(e.touches[0]);

window.onmousemove = e => handleOnMove(e);

window.ontouchmove = e => handleOnMove(e.touches[0]);

const imgs = document.querySelectorAll('#image-track img');



imgs.forEach(img => {
  var a = 0
  img.addEventListener('click', function() {
    if(a === 0) {
      img.style.height = '70vmin';
      img.style.width = '120vmin';
      img.style.padding = '0';
      img.style.zIndex = '0';
      a = 1;
    } else if(a===1) {
      setTimeout(()=>{a = 2}, 500);
      $(img).click(
        window.location.href = '#'
      );
    } else if(a===2) {
      img.style.width = '';
      img.style.height = '';
      img.style.padding = '';
      img.style.zIndex = '';
      a = 0;
    }
  });
});

