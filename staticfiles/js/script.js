// Bootstrap validation form script 
// I used Chat-GPT
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


// Initialize Flatpickr with functionality to limit time in accordance with the working schedule
// I used https://flatpickr.js.org/ and Chat-GPT

// Working hours 
const workHours = {
    weekdays: { from: "09:00", to: "22:00", days: [1, 2, 3, 4, 5] },
    weekend: { from: "12:00", to: "23:00", days: [6, 0] }
};

// Initialization of the choice of date
const datePicker = flatpickr("#date", {
    altInput: true,
    altFormat: "F j, Y",
    dateFormat: "Y-m-d",
    minDate: "today",
    onChange: updateTimeBasedOnDate // We update the time when changing the date
});

// Initialization of the choice of time
const timePicker = flatpickr("#time", {
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    time_24hr: true,
    minTime: "09:00",  // Initial values ​​for time
    maxTime: "22:00",
});

// Function for dates and time extracts, changes Mintime and Maxtime
function updateTimeBasedOnDate() {
    const date = datePicker.selectedDates[0];  // We extract the selected date
    if (!date) {
        console.error("Date is not chosen!");
        return;  // Interrupt the function if the date is not selected
    }
    const dayOfWeek = date.getDay();  // We get the day of the week
    
    // We determine which working hours apply
    let selectedWorkHours;
    if (workHours.weekdays.days.includes(dayOfWeek)) {
        selectedWorkHours = workHours.weekdays;
    } else if (workHours.weekend.days.includes(dayOfWeek)) {
        selectedWorkHours = workHours.weekend;
    }

    // Dynamically change Mintime and Maxtime for Flatpickr
    timePicker.set("minTime", selectedWorkHours.from);  // Update minTime
    timePicker.set("maxTime", selectedWorkHours.to);    // Update maxTime
}

// Calling the function immediately during initialization, to install the correct working hours for the initial date
updateTimeBasedOnDate();



// Table count for reservation form
// I used Chat-GPT
document.getElementById('people_count').addEventListener('input', function () {
    let peopleCount = parseInt(this.value);
    let tableCount = Math.ceil(peopleCount / 4);
    document.getElementById('table_count').value = tableCount;
});

