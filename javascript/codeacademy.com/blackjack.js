var twoRandomScores = function(){
    var score1 =  Math.floor(Math.random() * 10 + 1);
    var score2 =  Math.floor(Math.random() * 10 + 1);
    return score1 + score2;
}
var randomScore = Math.floor(Math.random() * 52 + 1);
console.log("I got the score " + randomScore);

var deal = Math.floor(Math.random() * 52 + 1);
var final = deal % 13;
console.log(final);