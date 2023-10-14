const scroll = new LocomotiveScroll({
    el: document.querySelector('#main'),
    smooth: true
});


function toggleMenu() {
  const menu = document.querySelector(".menu-links");
  const icon = document.querySelector(".hamburger-icon");
  menu.classList.toggle("open");
  icon.classList.toggle("open");
}
toggleMenu()

function profilepicAnime() {
  var photo = document.querySelector("#profilepic");
  photo.addEventListener("mouseenter", function() {
    photo.style.cursor = "grab";
  });
}

profilepicAnime()

function loadingAnimation(){
  gsap.from("#profile > div.section__text > h1", {
    y: 100,
    opacity: 0,
    delay: 0.5,
    duration: 0.9,
    stagger: 0.3,
  });
}
loadingAnimation()