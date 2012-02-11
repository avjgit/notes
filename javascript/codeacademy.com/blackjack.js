// Our deal function will return a random card
function deal() {
    card = Math.floor(Math.random()*52+1);
    return card;
}

// Deal out our first hand
var card1 = deal();
var card2 = deal();

// Make a getValue function here, which should convert a card to
// the value that card is worth
var getValue = function(card){
    return card%13;
}

// Our score function converts our cards to a score
var score = function () {
    return getValue(card1) + getValue(card2);
};

console.log("You have cards " + card1 + " and " + card2 +
        " for a score of " + score());