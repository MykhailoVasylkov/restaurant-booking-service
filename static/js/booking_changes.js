const editButtons = document.getElementsByClassName("btn-warning");
const bookingPhone = document.getElementById("phone_number");
const bookingDate = document.getElementById("date");
const bookingTime = document.getElementById("time");
const bookingNumPeople = document.getElementById("people_count");
const bookingNumTable = document.getElementById("table_count");
const bookingComment = document.getElementById("comment");
const bookingForm = document.getElementById("bookingForm");
const submitButton = document.getElementById("submitButton");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        // Get the booking ID from the data-booking_id attribute
        let bookingId = e.target.getAttribute("data-booking_id");

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