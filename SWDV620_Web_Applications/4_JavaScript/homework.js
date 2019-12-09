// 1. Write a script to prompt for a username and password.
function getUserLoginData() {
    var username = prompt('Please enter your username:');
    var passowrd = prompt('Please enter your password:');
}
getUserLoginData();


// 2. Provide a list of objects that can be used in Javascript and provide an example of each.
/**
 * I am not quite sure what the question is asking, as all data types in JavaScript inherit from
 * the JavaScript object. However, examples of objects include the Date, Math, and Navigator.
 * 
 * If 'list of objects' is referring to data types, there are the following:
 * String
 * Number
 * Boolean
 * Object
 * Array
 * null
 * undefined
 */

// Date object
var date = new Date();
console.log(date.getDate());

// Math object
var pi = Math.PI;

// Navigator object
var userAgent = navigator.userAgent;

// data types
// string
var s = 'foo';

// number
var n = 100;

// boolean
var b = true;

// object
var o = {}

// array
var a = [];

// null
var n = null;

// undefined
var u;


// 3. Choose a Javascript event and provide a code example.
// example: click event
var numOfClicks = 0,
    btn = document.createElement('button');
btn.innerText = 'click me';
btn.onclick = function btnClickHandler(event) {
    event.target.innerText = `clicked ${++numOfClicks} time${numOfClicks > 1 ? 's' : ''}`
}
document.body.append(btn);
