// Bootstrap validation script

(function () {
    'use strict'
    const forms = document.querySelectorAll('.needs-validation');
    Array.from(forms).forEach(form => {
        form.addEventListener('submit', event => {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
})();


// Initialize Flatpickr

document.addEventListener("DOMContentLoaded", function () {
    console.log(document.querySelector("#date")); // Теперь должен вернуть <input id="date">
    
    flatpickr("#date", {
        dateFormat: "Y-m-d",
        altInput: true,
        altFormat: "F j, Y",
        allowInput: true,
    });

    flatpickr("#time", {
        enableTime: true,
        noCalendar: true,
        dateFormat: "H:i",
        allowInput: true,
    });

    document.querySelector("#date").setAttribute("placeholder", "Select a date");
    document.querySelector("#time").setAttribute("placeholder", "Select a time");
});



// Table count for reservation form

document.getElementById('people_count').addEventListener('input', function () {
    let peopleCount = parseInt(this.value);
    let tableCount = Math.ceil(peopleCount / 4);
    document.getElementById('table_count').value = tableCount;
});