// Getting the elements for the stars and hidden input
const stars = document.querySelectorAll('.star');
const ratingInput = document.getElementById('rating-value');
const ratingGroup = document.getElementById('rating-group');
const form = document.getElementById('reviewForm');

// Handler for clicks on the stars
stars.forEach(star => {
    star.addEventListener('click', (e) => {
        // Get the rating value from the clicked star
        const rating = e.target.getAttribute('data-value');
        ratingInput.value = rating; // Set the value in the hidden input

        // Update the appearance of the stars based on the selected rating
        updateStars(rating);

        // Remove the 'is-invalid' class from the rating group (removes error) when a valid rating is selected
        ratingGroup.classList.remove('is-invalid');
    });

    // Change color on hover for all previous stars
    star.addEventListener('mouseover', (e) => {
        // Get the rating value on hover
        const rating = e.target.getAttribute('data-value');
        // Update the star colors based on the hovered rating value
        updateStars(rating);
    });

    // Reset stars to the selected rating when not hovering
    star.addEventListener('mouseout', () => {
        // Update the stars based on the current value in the hidden input field
        updateStars(ratingInput.value);
    });
});

// Function to update the appearance of stars based on the rating value
function updateStars(rating) {
    stars.forEach(star => {
        // If the star's data-value is less than or equal to the selected rating, mark it as selected (highlight it)
        if (star.getAttribute('data-value') <= rating) {
            star.classList.add('selected');
        } else {
            star.classList.remove('selected'); // Otherwise, remove the selected class (unhighlight)
        }
    });
}

// Form validation before submission
form.addEventListener('submit', (event) => {
    const ratingValue = ratingInput.value; // Get the rating value from the hidden input
    
    // If no rating is selected, prevent form submission and show an error
    if (ratingValue === '0') {
        event.preventDefault(); // Prevent form submission
        ratingGroup.classList.add('is-invalid'); // Add 'is-invalid' class to indicate an error
    }
});

// Check if a rating was selected after the page loads (in case the form is not submitted yet)
window.addEventListener('load', () => {
    const currentRating = ratingInput.value; // Get the rating value from the hidden input
    if (currentRating !== '0') {
        // If a rating was already selected, update the star colors to reflect the current rating
        updateStars(currentRating);
    }
});
