// Define a function called deal
// It should return a random number between 1 and 52
var deal = function(){
    var card = Math.floor(Math.random() * 52 + 1);
    return card;
}

// Declare two variables 
// For both variables, assign values gotten by calling the function
var card1 = deal();
var card2 = deal();