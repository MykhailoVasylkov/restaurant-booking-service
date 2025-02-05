const editButtons = document.getElementsByClassName("btn-warning");
const bookingPhone = document.getElementById("phone_number");
const bookingDate = document.getElementById("date");
const bookingTime = document.getElementById("time");
const bookingNumPeople = document.getElementById("people_count");
const bookingNumTable = document.getElementById("table_count");
const bookingComment = document.getElementById("comment");
const bookingForm = document.getElementById("bookingForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-danger");
const deleteForm = document.getElementById("deleteForm");


/* I used CodeStar project as a reference and Chatgpt

/**
 * Initializes edit functionality for the provided edit buttons.
 * 
 * For each button in the `editButtons` collection:
 * - Retrieves the associated booking's ID upon click.
 * - Fetches the content of the corresponding booking.
 * - Populates the form filds with the bookings's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_booking/{bookingId}` endpoint.
 */

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        // Get the booking ID from the data-booking_id attribute
        let bookingId = e.target.getAttribute("data-booking-id");

        // Get the comment content
        let bookingCommentValue = document.getElementById(`booking-comment${bookingId}`);
        if (bookingCommentValue) {
            bookingComment.value = bookingCommentValue.innerText;
        } else {
            // Leave the field empty if there is no comment
            bookingComment.value = "";
        }

        // Fill in the other form fields using the booking data
        let bookingPhoneValue = document.getElementById(`phone${bookingId}`).innerText;
        bookingPhone.value = bookingPhoneValue;

        let bookingDateValue = document.getElementById(`date${bookingId}`).innerText;
        bookingDate.value = bookingDateValue;

        let bookingTimeValue = document.getElementById(`time${bookingId}`).innerText;
        bookingTime.value = bookingTimeValue;

        let bookingNumPeopleValue = document.getElementById(`people_count${bookingId}`).innerText;
        bookingNumPeople.value = bookingNumPeopleValue;

        let bookingNumTableValue = document.getElementById(`table_count${bookingId}`).innerText;
        bookingNumTable.value = bookingNumTableValue;

        // Update the text on the button
        submitButton.innerText = "Update";

        // Update the form action for editing
        bookingForm.setAttribute("action", `edit/${bookingId}`);
    });
}


/**
 * Initializes deletion functionality for the provided delete buttons.
 * 
 * For each button in the `deleteButtons` collection:
 * - Retrieves the associated booking's ID upon click.
 * - Updates the `deleteConfirm` link's href to point to the 
 * deletion endpoint for the specific booking.
 * - Displays a confirmation modal (`deleteModal`) to prompt 
 * the user for confirmation before deletion.
 */

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let bookingId = e.target.getAttribute("data-booking-id");
        deleteForm.setAttribute("action", `delete/${bookingId}`);
        
        deleteModal.show();
        
    });
}