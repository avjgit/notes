// Getting Started with Programming
// lesson 1
"AJ"
"AJ".length
2+2
2*2
AJ
// lesson 2
confirm("see my question?")
alert("this is a alert!")
// lesson 3
myName
var myName
myName = 'AJ'
myName
var lastName = 'J'
var myFullName = myName + lastName
myFullName.length
// lesson 4
var number = 42
number/2
number%10
var myString = 'hello'
myString.substring(0, 2)
var three = 'Andrey'.substring(0,3)
'coding rules'.replace('coding', 'programming')
three.toUpperCase()
// lesson 5
var today = 'Monday'
var number = array[2]
array[2] = number
var numbers = [1, 2, 3];
var days = [];
days[0] = 'Monday';
days[1] = 'Tuesday';
days[2] = 'Wednesday';
// lesson 6

var number = 7;
if( number === 7 ) {
  console.log( "you typed a 7!" );
}

var name = "Annie";
if (name === "Sam") {
  console.log("Your name is Sam!"); }
else {
  console.log("Your name isn't Sam!"); 
};

var name;
// Prompt for the user's name here.
name = prompt("what's your name?");

if(name === "Sam") {
  console.log("Your name is Sam!");
} else{
  console.log("Your name isn't Sam!");
};

var number = prompt("Guess what number I'm thinking of between 1 and 10!");
if(number === "7") {
  console.log("You got it!");
// Change the following line.
} else if (number === "6") {
  console.log("Close! Try guessing a little higher.");
} else {
  console.log("You were way off! Sorry...");
}

var word = "that";
if( word === "that" ) {
  console.log( "word is equal to 'that'" );
}

var number = prompt( "pick a number between 1 and 10!" );
if( number === 5 ) {
  console.log( "your number is 5" );
}
else if ( number > 5 ) {
  console.log( "your number is greater than 5" );
}
else if ( number < 5 ) {
  console.log( "your number is less than 5" );
}

var response = prompt("Do you like me?");
if (response === "yes") {
  console.log("I like you too!");
}

// lesson 7
var i = 0;
i++;
i++;
console.log( "i is equal to " + i );

var i = 2;
i--;
i--;
console.log( "i is equal to " + i );

var i;
for (i = 0; i < 2; i++) {
  console.log("i is now equal to " + i);
}
console.log("i is now equal to " + i);

var i;
for ( i = 2 ; i > 0; i-- ) {
  console.log( "i is now equal to " + i );
};
console.log( "i is now equal to " + i );

// lesson 8
var i = 0;
while ( i < 2 ) {
  console.log( "i is now " + i );
  i++;
}

var i = 0;
while (i<2 ) {
  console.log( "hello" );
  i++;
};

var times = 0;
while (times > 0 && times < 3) {
  console.log("the loop ran");
  times++;
}

var i = 0;
do {
  console.log("This is iteration " + (i + 1) + ".");
  i++;
}
while(i<4 );

// fizzbuzz
for(i=1;i<21;i++){
    console.log(i);
}

for ( i=1; i<=20; i++) { 
  
  // if the number is divisible by 3, write "Fizz"
  if (i%3==0 ) { 
    console.log("Fizz");
  }
  
  // otherwise, write just the number
  else {
      console.log(i);
    
  }
}

// for the numbers 1 through 20,
for (i=1; i<=20; i++) { 
  
  // if the number is divisible by 3, write "Fizz"
  if ( i % 3 === 0 ) { 
    console.log("Fizz");
  }
  else if(i%5===0)
  // if the number is divisible by 5, write "Buzz"
  {
      console.log("Buzz");    
  }
  
  // otherwise, write just the number
  else {
    console.log(i);
  }
}

for (i=1; i<=20; i++) { 
  
  if (i%3===0 && i%5===0){
      console.log("FizzBuzz");
  }
  // if the number is divisible by 3, write "Fizz"
  else if ( i % 3 === 0 ) { 
    console.log("Fizz");
  }
  else if(i%5===0)
  // if the number is divisible by 5, write "Buzz"
  {
      console.log("Buzz");
  }
  
  // otherwise, write just the number
  else {
    console.log(i);
  }
}

// Add an else statement in case the number is divisible by 5. 
var upper_limit = prompt("count till...");
// for the numbers 1 through 20,
for (i=1; i<=upper_limit; i++) { 
  
  if (i%3===0 && i%5===0){
      console.log("FizzBuzz");
  }
  // if the number is divisible by 3, write "Fizz"
  else if ( i % 3 === 0 ) { 
    console.log("Fizz");
  }
  else if(i%5===0)
  // if the number is divisible by 5, write "Buzz"
  {
      console.log("Buzz");
  }
  
  // otherwise, write just the number
  else {
    console.log(i);
  }
}

// Functions
// 1-1
var hello = function () {
  // Print hello on the console.
  console.log("i am saying hello");
};

hello();
hello();

//1-2
var hi =function () {
  console.log("hi");
};

hi();

//1-3
var myFirstFunction =function(){
    console.log("yourName");
}

myFirstFunction();

//1-4
var fullName = "";
var name;
var firstLetter;
var fixName= function(){
    firstLetter = name.substring(0, 1);
    name = firstLetter.toUpperCase() + name.substring(1);
    fullName = fullName + " " + name;
}
name = prompt("Enter your first name (all in lower case):");
fixName();
name = prompt("Enter your second name (all in lower case):");
fixName();
console.log("And your full name is:" + fullName);

// Lesson 2 Variables
var greeting = "Ahoy";


//variables do not have to be declared before the function is defined, just before the function is called!
var greeting = "Ahoy";
var greet = function(){
    var greeting = "Hello";
    console.log(greeting);
}
greet(); // put Hello
console.log(greeting); // put Ahoy


var sayHelloTo = function (name) {
  console.log("Hello " + name);
};

sayHelloTo("AJ");




/* Start global variable `greeting` scope */
var greeting = "Ahoy";

var greet = function () {
  /* Start local variable `greeting` scope */
  var greeting = "Hello";
  
  /* Start local variable `myName` scope */
  var myName = prompt("Input your name: ");
  
  console.log(greeting + " " + myName);
  
  /* End local variables `myName` and `greeting` scope */
};

greet();

// This will produce a `ReferenceError` since we are out
// of the `myName` variable scope.
console.log(myName);




var square = function (x) {
  return x*x;
};
square();




var identity = function (x) {
  
  return x;
};
identity();




var isEven = function (n) {
  if (n % 2 === 0) {
    return true;
  } else {
    return false;
  }
};

console.log(isEven(1));
console.log(isEven(2));
console.log(isEven(999));




var lost = [4, 8, 15, 16, 23, 42];
var count = lost.length;

var isLost = function (n) {
  for (i=0;i<=count;i++ ) {
    if ( n === lost[i]) {
      return true;
    }
  }
  return false;
};

if ( isLost(12) ) {
  console.log('12 is a lost number');
}

if ( isLost(16) ) {
  console.log('16 is a lost number');
}




var quarter = function(n){
    return n/4;
}

if (quarter(4) === 1) {
  console.log("The statement is true.");
} else {
  console.log("The statement is false.");
}




var cube = function(x){
    return x*x*x;
}
cube(3);




var square = function (x) {
  return x * x;
};

var cube = function (x) {
  return square(x) * x;
};




var isMultipleOfThree = function (x) {
  return x % 3 === 0;
};

var isNotMultipleOfThree = function (x) {
  return !isMultipleOfThree(x);
};





var isOdd = function(x){
    if(x%2 === 0){
        return false;
    } else {
        return true;
    }    
};

var isEven = function(x){
    return !isOdd(x);
};




var area = function (w, l) {
  return w*l;
};




var isDivisible = function (x, y) {
    if (x%y === 0){
        return true;
    }else {
        return false;
    }
};




var power = function (base, exponent) {
  var result = 1;
  for (var i = 0; i < exponent; i++) {
    result = result * base;
  }
  return result;
};

power(2, 2);




var power = function(base, exponent){
    if(exponent === 0){
        return 1;
    }    else{
        return base * power(base, exponent-1);
    }
}

console.log(power(2, 4) === 16);
console.log(power(2, 0) === 1);
console.log(power(2, 1) === 2);




var taxiFare = function (milesTraveled, hourOfDay) {
  var baseFare = 2.50;
  var costPerMile = 2.00;
  var nightSurcharge = 0.50; // 8pm to 6am, every night

  var cost = baseFare + (costPerMile * milesTraveled);
  
  if (hourOfDay >= 20 || hourOfDay < 6){
      cost += nightSurcharge;
  }
 
  return cost;
};
var tripCost =  taxiFare(5, 2);




// Accepts a number x as input and returns its square
var square = function(x) {
  return x * x;
}

// Accepts a number x as input and returns its cube
var cube = function(x) {
  return x * square(x);
}

cube(7);




var multiply = function (x, y) {
   return x * y;
}

multiply(2, 5);

var volume = function (w, l, h ) {
  return w * l * h;
}

volume(2, 3, 4);




// Change the argument name from x to n
var cube = function (n) {
  if (typeof(x) != 'number') return 0;
  return n * n * n;
}

// When you call cube with the new argument name, it
// should still return the same result.
cube(5);
console.log(cube("test"));




var w = 15;

var volume = function (w, l, h) {
   return w * l * h;
}

volume(2, 3, 4);
console.log(w);



var area = 36;
var volume = function (w, l, h) {
  // global var can be modified
  // area = w * l;
  var area = w * l;
  return area * h;
}


console.log(volume(2, 3, 4));
console.log(area);




// 1. prompt for name
var runner = prompt("What is your name?");

// 2. write condition to ensure runner is not empty
    if (runner.length > 0 ) { 
	  console.log("Welcome to the Olympic tryouts, " + runner);
  } else {
	  console.log("Name cannot be blank.");
  }
var raceTimes = [12.2,11.8,12.5,10.9,11.1];
var totalTime = 0;

for ( i = 0; i < raceTimes.length; i++ ) {
    totalTime += raceTimes[i];
}

var averageTime = totalTime/ raceTimes.length;




// runner times
// Runner times
var carlos = [9.6,10.6,11.2,10.3,11.5];
var liu = [10.6,11.2,9.4,12.3,10.1];
var timothy = [12.2,11.8,12.5,10.9,11.1];

var calculateAverage = function (raceTimes) {
  for ( i = 0; i < raceTimes.length; i++ ) {
    var totalTime = (totalTime || 0) + raceTimes[i];
  }
  var averageTime = totalTime/ raceTimes.length;    
  return averageTime;
};

var isQualified = function (runner) {
  var averageTime = calculateAverage(runner);
    
  if ( averageTime >= 11.5 ) { 
    // Times greater than or equal to 11.5 are too slow
	console.log("Close, but you didn't make the cut.");
  } else if ( averageTime < 11.5 ) {
	// An average time of less than 11.5 can join the team
	console.log("Welcome to the team, speedy!");
  }
};

isQualified(liu);
isQualified(timothy);

// Call the function isQualified on liu and timothy




//Review on finding the length of strings and variables

var name = "Leng Lee";
var number = name.length;
console.log(number);




var i = 0;
while (i === 0) {
  console.log("Hello");
  i++;
}




var familyIncome = function(mumIncome, dadIncome) {
  return mumIncome + dadIncome;
};

familyIncome(100000, 100000);




var yourName = "";
var result = "";
// use the > symbol to check the length of yourName
if ( yourName.length > 0) {
   result = "Hi "+ yourName;
} else {
   result = "What is your name?"
};




var yourName = "AJ";
var gender = "male";
var result;

if (gender === "male") {
  result = "His name is "+yourName;
} else if (gender === "female") {
  result = "Her name is "+yourName;
} else {
  result = "Hi "+yourName;
}




var checkNameGender = function (yourName,gender) {
//All the code below was used in exercise 1.6
  
    if (gender.length > 0 && yourName.length > 0) {
      if (gender === 'male' || gender === 'female') {
            return true;
      } else {
            return false;
      }
    } else {
      return false;
    }
};
checkNameGender("AJ", "male");




var canIDrive = function(myAge, legalDrivingAge){
    return myAge >= legalDrivingAge;
};
var myAge = prompt("How old are you?");
var legalDrivingAge = 18;

if (canIDrive(myAge, legalDrivingAge)) {
  console.log("You can legally drive!");
}
else {
  console.log("You'll have to wait a few more years!");
}




var jacketColor = "black";
var result;

switch (jacketColor) {
    
  case "black":
    result = "Pay $300";
    break;
    
  case "brown":
    result = "Pay $200";  
    break;
    
  case "green":
    result = "Pay $5";
    break;
    
  default:
    result = "This color does not match my eyes!";
}




var myCar = "Toyota" ;
var result;

switch (myCar) {
    
  case "Ford":
    result = "American brand";
  break;
  
  case "Toyota":
    result  = "Japanese brand";
  break;
    
  default:
    result = "I'm not sure what country that car is from";
  break;  
}




var born = prompt("What country were you born in?")
var result = "";

switch (born) {
    case "USA":
        result = "Born in the USA";
    break;
    
    default:
        result = "Born outside the USA";
    break;   
}




var born = prompt("What country were you born in?");
var result;

// write the whole switch statement 
switch(born){
    case "USA":
        result = 1;
    break;
    
    case "England":
        result = 2;
    break;
    
    default:
        result = 3;
    break;
}




var myAge = prompt("What's your age?");

// a simple if else statement
if (myAge >= 18) {
 answer = "";
}
else {
 answer = "non-adult" ;
}

// rewrite the code above using a ternary operator
answer = myAge > 18 ? "adult" : "non-adult";




var name = prompt("What's your name?")

//Rewrite the above code using the ternary operator
result = name === "Nick" ? true : false;




var food = prompt("Which food?");

//Re-write the above code using a ternary operator
foodType = food === "taco" ? "Mexican" : "other";




var gender = "male";

if (gender === "female") {
  result = "true";
}
else {
  result = "false"
}




var cost = 101;
var employed = "yes";
var result;

if (cost > 100) {
  if (employed === "yes") {
  result = "buy";
  } else { 
  result = "can't afford";
  }
} 
else {
  result = "reject cheap product";
}




var topThree = "true";
var winner = "true";
var result;

if (topThree === "false") {
  result = "Sorry, empty handed";
}
else {
  if (winner === "true") {
    result = "Gold!!!";
  } else {
    result = "Not bad! Got a medal!";
  }
}




var x = 10
var y = 9

//The ternary operator in action
//result = x > y ? "good job" : 20;

//Rewrite the ternary code using if else statements
if ( x > y){
    result = "good job";
}else{
    result = 20;
}




// pick a random number between 1 and 6 for our roll of the die
var die1 = Math.floor(Math.random()*6 + 1);
var die2 = Math.floor(Math.random()*6 + 1);
var score;

// This time if either die roll is 1 then score should be 0 
if(die1 === 1 || die2 === 1){
    score = 0;
} else if (die1 === die2){
    score = (die1+die2)*2;
} else {
    score = die1 + die2;
}

console.log("You rolled a "+die1+" and a "+die2+" for a score of "+score);




var calculateTotalCosts = function(salary, numWorkers, city) {
  var fixedCosts = 5000;
  var variableCosts = salary * numWorkers;
  
  if (city === "NYC") {
    return fixedCosts + variableCosts + 30000;
  }
  else if (city === "BEJ") {
    return fixedCosts + variableCosts + 25000;
  }
  else {
    return fixedCosts + variableCosts + 10000;
  };
};
  
console.log(calculateTotalCosts(50000, 9, "NYC"));
console.log(calculateTotalCosts(50000, 9, "BEJ"));
console.log(calculateTotalCosts(50000, 9, "MUM"));




var yourJob = "developer";
var dominantHand = "right";
var result;

//Line 10 starts an if statement
//Nested in this if statement is an if else statement on lines 11 - 15
//This nested if else statement allows us to check another condition
//We close the first if statement at the start of line 16

if (yourJob.length > 0 && dominantHand.length > 0) {
  if (dominantHand === "right" || dominantHand === "left") {
    result = "Thanks";
  } else {
	result = "Please enter right or left for dominantHand.";
  }
} else {
  result = "Please tell us both your job and your dominant hand.";
}

console.log("Parentheses for conditions, curly for code.");
console.log("Function code goes between curly brackets.");
console.log("Use semi-colons in 3 situations.");
console.log("No semi-colons in loops or conditionals!");




"can"+"can"
var number = 10;
console.log("I think I am 10 out of " + number);
"Hi" === "hi"
console.log( 2 >= 1 ); // is greater than or equal to.
console.log( 4 > 1 ); // is greater than.
console.log( 0 === 0); // is equal to.
console.log( 1 <= 1 ); // is less than or equal to.
console.log( "Hi" !== "hi" ); // is not equal to.
console.log( 0 < 1 ); // is less than.
true && !false;
false || ( 5 === 2 + 4 );




var x = 1;
var y = 2;

if (y>x ) {
  console.log('y is larger than x');
}




// Write a statement that decides if the variable `i` is divisible by 3.  

// for the numbers 1 through 20,
for ( i=1; i<=20; i++) { 

  // if the number is divisible by 3 *and* 5, write "FizzBuzz" 
  if ((i%3 === 0) && (i%5 === 0) ) { 
    console.log("FizzBuzz");
  // if the number is divisible by 3 write "Fizz" 
  } else if (i%3 === 0) {
    console.log("Fizz");
  // if the number is divisible by 5 write "Buzz" 
  } else if (i%5 === 0) {
    console.log("Buzz");
  // otherwise, write just the number
  } else {
    console.log(i);
  }
}




var numbers = [1, 2, 3];
var animals = ["cat", "dog", "monkey"];


// Then we'll print them out one by one
console.log(animals[0]);
console.log(animals[1]);
console.log(animals[2]);