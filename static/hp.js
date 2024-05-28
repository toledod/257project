document.addEventListener('DOMContentLoaded', () => {
    const textContainer = document.getElementById('songNameHome');
    const newText = 'This is the new text.';

    // Change text after 3 seconds
    setTimeout();
        // Add the fade-out class
    textContainer.classList.add('fade-out');

        // Wait for the transition to complete (1 second), then change the text and fade in
    function setTimeout() {
        textContainer.textContent = newText;
        textContainer.classList.remove('fade-out');
    }
    });
