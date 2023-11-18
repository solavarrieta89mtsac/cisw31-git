// Salvador M. Olavarrieta
// Happy Birthday
//11/14/2023

// Is it Your birthday?
// Determine whether today is the date entered
// and display happy birthday if it

// Set birthday manually
let bday = new Date(1986, 10, 11);
let bd_month = bday.getMonth();
let bd_day = bday.getDate();

let today = new Date();
let month = today.getMonth();
let day = today.getDate();

// check if the month and day are the same
if ( day == bd_day && month == bd_month) {
    console.log("🎂 Happy Birthday! 🥳");
} else {
    console.log("It's not your birthday.")
}