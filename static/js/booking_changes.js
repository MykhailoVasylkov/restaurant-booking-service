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
        // Получаем ID бронирования из атрибута data-booking_id
        let bookingId = e.target.getAttribute("data-booking_id");

        // Получаем содержимое комментария
        let bookingCommentValue = document.getElementById(`booking-comment${bookingId}`);
        if (bookingCommentValue) {
            bookingComment.value = bookingCommentValue.innerText;
        } else {
            bookingComment.value = ""; // Оставляем поле пустым, если комментария нет
        }

        // Заполняем другие поля формы, используя данные из бронирования
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

        // Обновляем текст на кнопке
        submitButton.innerText = "Update";

        // Обновляем action формы для редактирования
        bookingForm.setAttribute("action", `booking/edit/${bookingId}`);
    });
}
