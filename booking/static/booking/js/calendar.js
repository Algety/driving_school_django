// let calendarEl = document.getElementById('calendar');
// let calendar = new Calendar(calendarEl, {
//   plugins: [ dayGridPlugin, timeGridPlugin, listPlugin ],
//   initialView: 'dayGridMonth',
//   headerToolbar: {
//     left: 'prev,next today',
//     center: 'title',
//     right: 'dayGridMonth,timeGridWeek,listWeek'
//   }
// });
// calendar.render();

document.addEventListener('DOMContentLoaded', function() {
    var calendarEl = document.getElementById('calendar');
    if (!calendarEl) return;

    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'dayGridMonth',
        selectable: true,
        headerToolbar: {
            left: 'prev,next today',
            center: 'title',
            right: 'dayGridMonth,timeGridWeek,listWeek'
        },
        select: function(info) {
            var selectedDate = new Date(info.startStr);
            var today = new Date();
            today.setHours(0, 0, 0, 0); // Reset time to compare dates

            // Restrict selection to tomorrow or later
            if (selectedDate <= today) {
                alert("Please pick a date starting from tomorrow.");
                return;
            }

            // Ask for a lesson time
            let selectedTime = prompt("Choose an hour (8:00 - 20:00):", "8:00");
            if (selectedTime) selectedTime = selectedTime.trim();

            // Validate time input (must be within range)
            let validHours = Array.from({ length: 13 }, (_, i) => (8 + i) + ":00");
            if (selectedTime && validHours.includes(selectedTime)) {
                let dateInput = document.getElementById("selected_date");
                let timeInput = document.getElementById("selected_time");
                if (dateInput && timeInput) {
                    dateInput.value = info.startStr;
                    timeInput.value = selectedTime;
                    alert("Booking selected: " + info.startStr + " at " + selectedTime);
                }
            } else {
                alert("Invalid time selection. Choose between 8:00 and 20:00.");
            }
        }
    });

    calendar.render();
});

