window.onload = () => {
    document.querySelectorAll('.card').forEach((card, index) => {
        card.style.animationDelay = `${index * 0.2}s`;
    });
}
// =====================================================
// LIVE CLOCK
// =====================================================

function updateClock(){

    const now = new Date()

    const time = now.toLocaleTimeString()

    const options = {
        weekday:'long',
        year:'numeric',
        month:'long',
        day:'numeric'
    }

    const date = now.toLocaleDateString(
        undefined,
        options
    )

    document.getElementById(
        "live-clock"
    ).innerHTML = `${date} • ${time}`
}

setInterval(updateClock,1000)

updateClock()

// =====================================================
// GREETING
// =====================================================

const hour = new Date().getHours()

let greeting = "Welcome"

if(hour < 12){

    greeting = "Good Morning"

}else if(hour < 18){

    greeting = "Good Afternoon"

}else{

    greeting = "Good Evening"
}

document.getElementById(
    "greeting-text"
).innerHTML = greeting