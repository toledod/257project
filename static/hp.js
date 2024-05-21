function updateDays2() {
  month = document.getElementById('month').value;
  daySelect = document.getElementById('day');
  daysInMonth = new Date(2024, month, 0).getDate(); 
  
  let options = '';
  for (let day = 1; day <= daysInMonth; day++) {
    options += `<option value="${day}">${day}</option>`;
  }
  daySelect.innerHTML = options;
  document.addEventListener('DOMContentLoaded', updateDays);
}
