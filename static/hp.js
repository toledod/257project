function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function setRandomColor() {
  the_heading = document.getElementById("hello");
  the_heading.style.color = getRandomColor()
  console.log("I just changed the color to: " + the_heading.style.color)  
}
