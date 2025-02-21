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
// Does not work on mobile devices
// I used https://flatpickr.js.org/ and Chat-GPT

// Working hours 
const workHours = {
    weekdays: {
        from: "09:00",
        to: "23:30",
        days: [1, 2, 3, 4, 5]
    },
    weekend: {
        from: "12:00",
        to: "23:00",
        days: [6, 0]
    }
};

// Initialization of the choice of date
const datePicker = flatpickr("#date", {
    dateFormat: "Y-m-d",
    minDate: "today",
    disable: [disableTodayIfClosed], // Function to disable today's date if needed
    onChange: function (selectedDates) {
        if (selectedDates.length > 0) {
            updateTimeBasedOnDate();
        }
    } 
});

// Initialization of the choice of time
const timePicker = flatpickr("#time", {
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    time_24hr: true,
    minTime: "09:00", // Initial values ​​for time
    maxTime: "22:00",
});

// Function to disable today if working hours are over
function disableTodayIfClosed(date) {
    const today = new Date();
    if (date.toDateString() !== today.toDateString()) return false; // Only check today

    const dayOfWeek = today.getDay();
    let selectedWorkHours;

    if (workHours.weekdays.days.includes(dayOfWeek)) {
        selectedWorkHours = workHours.weekdays;
    } else if (workHours.weekend.days.includes(dayOfWeek)) {
        selectedWorkHours = workHours.weekend;
    }

    const closingTime = selectedWorkHours.to.split(":"); // [HH, MM]
    const closingHour = parseInt(closingTime[0], 10);
    const closingMinute = parseInt(closingTime[1], 10);

    // Get current time
    const currentHour = today.getHours();
    const currentMinute = today.getMinutes();

    // Disable today if current time is past closing time
    return currentHour > closingHour || (currentHour === closingHour && currentMinute > closingMinute);
}

// Function to update minTime and maxTime based on the selected date
function updateTimeBasedOnDate() {
    const date = datePicker.selectedDates[0]; // Extract the selected date
    if (!date) {
        console.error("Date is not chosen!");
        return; // Stop the function execution if no date is selected
    }
    const dayOfWeek = date.getDay(); // Get the day of the week

    // Determine which working hours apply
    let selectedWorkHours;
    if (workHours.weekdays.days.includes(dayOfWeek)) {
        selectedWorkHours = workHours.weekdays;
    } else if (workHours.weekend.days.includes(dayOfWeek)) {
        selectedWorkHours = workHours.weekend;
    }

    let minTime = selectedWorkHours.from; // Initial value for minTime

    // Check if the selected date is today
    const today = new Date();
    if (date.toDateString() === today.toDateString()) {
        const currentTime = new Date();
        currentTime.setMinutes(currentTime.getMinutes() + 30); // Add 30 minutes to the current time

        const hours = currentTime.getHours().toString().padStart(2, '0');
        const minutes = currentTime.getMinutes().toString().padStart(2, '0');
        minTime = `${hours}:${minutes}`; // Set minTime to 30 minutes later than the current time
    }

    // Dynamically update minTime and maxTime for Flatpickr
    timePicker.set("minTime", minTime); // Update minTime
    timePicker.set("maxTime", selectedWorkHours.to); // Update maxTime
}



// Table count for reservation form
// I used Chat-GPT
document.addEventListener('DOMContentLoaded', function () {
    const peopleCountInput = document.getElementById('people_count');
    if (peopleCountInput) {
        peopleCountInput.addEventListener('input', function () {
            let peopleCount = parseInt(this.value);
            let tableCount = Math.ceil(peopleCount / 4);
            document.getElementById('table_count').value = tableCount;
        });
    }
});

//Smoothly hide and show the menu when a modal opens/closes
document.addEventListener("DOMContentLoaded", function () {
    const menu = document.querySelector('.sticky-cnt');

    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('show.bs.modal', function () {
            menu.classList.add('hidden'); // Smoothly hide the menu when the modal opens
        });

        modal.addEventListener('hidden.bs.modal', function () {
            setTimeout(() => {
                menu.classList.remove('hidden'); // Smoothly show the menu when the modal closes
            }, 100); // Small delay for a natural effect
        });
    });
});

// blocks the pile beyond the boundaries of the screen
document.addEventListener('touchmove', function(event) {
    if (window.innerWidth < window.outerWidth) {
        event.preventDefault(); 
    }
}, { passive: false });
