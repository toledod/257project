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

function updateDays() {
  month = document.getElementById('month').value;
  daySelect = document.getElementById('day');
  daysInMonth = new Date(2024, month, 0).getDate(); 
  
  let options = '';
  for (let day = 1; day <= daysInMonth; day++) {
    options += `<option value="${day}">${day}</option>`;
  }
  daySelect.innerHTML = options;
}

window.onload = updateDays;
