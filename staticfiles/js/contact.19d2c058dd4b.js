// Getting the elements for the stars and hidden input
const stars = document.querySelectorAll('.star');
const ratingGroup = document.getElementById('rating-group');

const ratingInput = document.getElementById('rating-value');
const form = document.getElementById('reviewForm');
const editButtons = document.getElementsByClassName('btn-warning');
const reviewBody = document.getElementById('review');
const submitButton = document.getElementById('submitButton');

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("delete-btn");
const deleteForm = document.getElementById("deleteForm");

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


/* I used CodeStar project as a reference and Chatgpt

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Fetches the content of the corresponding review.
 * - Populates the form filds with the review's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        // Get the review ID from the data-review_id attribute
        let reviewId = e.target.getAttribute("data-review-id");

        // Fill in the form fields using the review data
        let reviewRatingValue = document.getElementById(`rating-value-${reviewId}`).value;
        ratingInput.value = reviewRatingValue;

        // Call updateStars to visually fill the stars based on the rating
        updateStars(reviewRatingValue);

        let reviewBodyValue = document.getElementById(`body${reviewId}`).innerText;
        reviewBody.value = reviewBodyValue;

        // Update the text on the button
        submitButton.innerText = "Update";

        // Update the form action for editing
        form.setAttribute("action", `edit/${reviewId}`);
    });
}

/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated review's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific booking.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let reviewId = e.target.getAttribute("data-review-id");
        deleteForm.setAttribute("action", `delete/${reviewId}`);

        deleteModal.show();

    });
}

// Add Google Maps integration with a marker
// I used Chat-GPT and code from Django-Blog Project

async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

    const location = { lat: 53.345260, lng: -6.255139 };

    const map = new Map(document.getElementById("map"), {
        zoom: 15,
        center: location,
        mapId: "Napoli_Map",
    });

    const marker = new AdvancedMarkerElement({
        position: location,
        map: map,
    });

    // Create an info window with the work schedule
    const infoWindow = new google.maps.InfoWindow({
        content: `<div>
        <h4>Napoli Restaurant</h4>
            <h5>Open Hours</h5>
            <p>Monday - Friday: 09:00 - 22:00</p>
            <p>Saturday - Sunday: 12:00 - 23:00</p>
            <h6><i class="fa-solid fa-location-dot"></i> Address:</h6>
            <p>Dublin, Main Street, 1</p>
            <h6><i class="fa-solid fa-phone"></i> Phone:</h6>
            <p>+353876235418</p>
            <h6><i class="fa-solid fa-envelope"></i> Contact:</h6>
            <p>Dublin, Main Street, 1</p>
            <a href="mailto:info@napoli.com" class="margin mb-2">info@napoli.com</a>
        </div>`
    });

    // Add an event listener for a click on the marker
    marker.addListener("click", () => {
        infoWindow.open({
            anchor: marker,
            map: map,
        });

        // Set a timeout to show the confirmation prompt after a short delay
        setTimeout(() => {
            // Ask user if they want to open this location in Google Maps
            const userConfirmed = confirm("Do you want to open this location in Google Maps?");

            if (userConfirmed) {
                const googleMapsUrl = `https://www.google.com/maps/dir/?api=1&destination=${location.lat},${location.lng}`;
                window.open(googleMapsUrl, "_blank");
            }
        }, 500); // Delay in milliseconds before showing the prompt
    });
}
