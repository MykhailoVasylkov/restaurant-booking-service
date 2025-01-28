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

flatpickr("#date", {
    dateFormat: "Y-m-d",
    minDate: "today",
});

flatpickr("#time", {
    enableTime: true, 
    noCalendar: true,
    dateFormat: "H:i",
});