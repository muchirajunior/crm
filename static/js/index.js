console.log('Django CRM')
function getCurrentDate() {
    // Array of month names
    const monthNames = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];

    // Array of day names
    const dayNames = [
        "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
    ];

    // Get the current date
    const date = new Date();
    
    // Get the day name, date, month name, and year
    const dayName = dayNames[date.getDay()];
    const dayOfMonth = date.getDate();
    const monthName = monthNames[date.getMonth()];
    const year = date.getFullYear();

    // Format the date string
    return `${dayName}, ${dayOfMonth} ${monthName} ${year}`;
}

// Display the current date in an element with the ID 'current-date'
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('current_date').textContent = getCurrentDate();
});
