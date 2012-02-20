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
     fixedCosts + variableCosts + 30000;
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
// Here is an array of multiples of 5. But is it correct?
var multiplesOfFive = [5,10,15,22,25,30];

// Test to see if a number from the array is NOT a true
// multiple of five. Real multiples will return false.
multiplesOfFive[3] % 5 !== 0;





var score = Math.floor(Math.random()*20 + 1);
var score = Math.random();
console.log(score);

var score = 7.352;
score = Math.floor(score);
console.log(score);




// Write your full name
var myName = "AJ"

// And your age
var myAge = 29

// Are you a human? Be honest.
var iAmHuman = true; 

console.log("My name is " + myName + " and I am " + myAge + " years old.");




// This array has lots of different data types in it
var manyThings = ["peanut butter", 1972, "Teletubby", 13.2, true];

// Pick one item
var someThing = manyThings[4];

// And see what data type it is!
console.log(typeof someThing);




var primitive = "chocolate";

if ( primitive === "chocolate" ) {
    console.log("Mmm... chocolate.");
}

var primitive = 4

if ( primitive < 5 ) {
	console.log("That is a nice low number.");
}

var primitive = false

if ( !primitive === true ) {
	console.log("I am not not telling the truth.");
}




// Here is an array of multiples of 8. But is it correct?
var multiplesOfEight = [8,16,24,32,40,58];

// Test to see if a number from the array is NOT a true
// multiple of five. Real multiples will return false.
var answer = multiplesOfEight[5] % 8 !== 0;




for (i=1; i<=20; i++) { 
  
  
  // if the number is divisible by 3, write "Fizz"
  if ( i % 3 === 0 ) { 
    if (i%5===0){
      console.log("FizzBuzz");
    }else{
        console.log("Fizz");
    }
  } else if(i%5===0)
  // if the number is divisible by 5, write "Buzz"
  {
      console.log("Buzz");
  }  
  // otherwise, write just the number
  else {
    console.log(i);
  }
}




var getReview = function (movie) {
    switch(movie){
        case "Matrix":
            return "good trip out";
        break;
        case "Princess Bride":
            return "awesome date night movie";
        break;
        case "Welcome to America":
            return "Amjad's favorite";
        break;
        case"Remember the Titans":
            return "love the sports";
        break;
        case "Why do I look like I'm 12?":
            return "The Ryan and Zach story";
        break;
        case "Fighting Kangaroos in the wild": 
            return "Token Australian movie for Leng";
        break;
        default:
            return "I don't know!"
        break;
    }
};




var bob = {};
var Spencer = {
  age: 22,
  country: "United States"
};

var Me = {
    age: 29,
    country: "Latvia"
}
// Our bob object again, but made using a constructor this time 
var bob = new Object();
bob.name = "Bob Smith";
bob.age = 30;
// Here is susan again, in literal notation
var susan1 = {
  name: "Susan Jordan",
  age: 24
};
// Make a new susan2 object, using a constructor instead
var susan2 = new Object();
susan2.name = "Susan Jordan";
susan2.age = 24;




// Take a look at our next example object, a dog
var dog = {
  species: "greyhound",
  weight: 60,
  age: 4
};

var species = dog['species'];
// fill in the code to save the weight and age using bracket notation
var weight = dog['weight'];
var age = dog['age'];




// help us make snoopy using literal notation
// Remember snoopy is a "beagle" and is 10 years old.
var snoopy = {
    species: "beagle",
    age: 10
}

// help make buddy using constructor notation
// buddy is a "golden retriever" and is 5 years old
var buddy = new Object();
buddy.species = "golden retriever";
buddy.age = 5;




var bob = {
  name: "Bob Smith",
  age: 30
};
var susan = {
  name: "Susan Jordan",
  age: 25
};
// here we save Bob's information
var name1 = bob.name;
var age1 = bob.age;
// finish this code by saving Susan's information
var name2 = susan.name;
var age2 = susan.age;




var BMW = {
    cost: "too much",
    speed: 220,
    country: "Germany"
}




// Accepts a number x as input and returns its square
var square = function (x) {
  return x * x;
};

// Write the function multiply below
// It should take two parameters and return the product
var multiply = function(x, y){
    return x*y;
}
multiply(2,3);




// here is bob again, with his usual properties
var bob = new Object();
bob.name = "Bob Smith";
bob.age = 30;
// this time we have added a method, setAge
bob.setAge = function (newAge){
  bob.age = newAge;
};
bob.getYearOfBirth = function () {
  return 2012 - bob.age;
};
// here we set bob's age to 40
bob.setAge(20);
// bob's feeling old.  Use our method to set bob's age to 20





//this acts as a placeholder, and will refer to whichever object calls that method when the method is actually used.
// here we define our method using "this", before we even introduce bob
function setAge (newAge) {
  this.age = newAge;
};
// now we make bob
var bob = new Object();
bob.age = 30;
// and down here we just use the method we already made
bob.setAge = setAge;
  
// change bob's age to 50 here
bob.setAge(50);

// make susan here, and first give her an age of 25
var susan = new Object();
susan.age = 25;
susan.setAge = setAge;

// here, update Susan's age to 35 using the method
susan.setAge(35);




var rectangle = new Object();
rectangle.length = 3;
rectangle.width = 4;
// here is our method to set the length
rectangle.setLength = function (newLength) {
  this.length = newLength;
};
// help by finishing this method
rectangle.setWidth = function(newWidth){
    this.width = newWidth;
}
  

// here change the width to 8 and length to 6 using our new methods
rectangle.setLength(6);
rectangle.setWidth(8);





var square = new Object();
square.sideLength = 6;
square.calcPerimeter = function() {
  return this.sideLength * 4;
};
// help us define an area method here
square.calcArea = function(){
    return this.sideLength * this.sideLength;
}

var p = square.calcPerimeter();
var a = square.calcArea();




// here we make bob using the Object constructor
var bob = new Object();
bob.name = "Bob Smith";
// add bob's age here and set it equal to 20
bob.age = 20;




function Person(name,age) {
  this.name = name;
  this.age = age;
}

// Let's make bob and susan again, using our constructor
var bob = new Person("Bob Smith", 30);
var susan = new Person("Susan Jordan", 25);
// help us make george, whose name is "George Washington" and age is 275
var george = new Person("George Washington", 275);




function Cat(age, color) {
  this.age = age;
  this.color = color;
}

// make a Dog constructor here
function Dog(age, name){
    this.age = age;
    this.name = name;
}




function Person(name,age) {
  this.name = name;
  this.age = age;
  // default property
  this.species = "Homo Sapiens";
}

var sally = new Person("Sally Bowles", 39)
var holden = new Person("Holden Caulfield", 16)
console.log("sally's species is " + sally.species + " and she is " + sally.age);
console.log("holden's species is " + holden.species + " and he is " + holden.age);




function Rectangle(length, width) {
  this.length = length;
  this.width = width;
  this.calcArea = function() {
      return this.length * this.width;
  };
  // put our perimeter function here!
  this.calcPerimeter = function(){
      return (this.length + this.width) * 2;
  }  
}
var rex = new Rectangle(7,3);
var area = rex.calcArea();
var perimeter = rex.calcPerimeter();




// first we can make the instructor
function Rabbit(adjective) {
    this.adjective = adjective;
    this.describeMyself = function() {
        console.log("I am a " + this.adjective + " rabbit");
    };
}
// now we can easily make all of our rabbits
var rabbit1 = new Rabbit("fluffy");
var rabbit2 = new Rabbit("happy");
var rabbit3 = new Rabbit("sleepy");
console.log(rabbit1.describeMyself);
console.log(rabbit2.describeMyself);
console.log(rabbit3.describeMyself);




// Our Person constructor
function Person(name, age){
    this.name = name;
    this.age = age;
}
// Now we can make an array of people
var family = new Array();
family[0] = new Person("alice", 40);
family[1] = new Person("bob", 42);
family[2] = new Person("michelle", 8);
family[3] = new Person("timmy", 6);
// loop through our new array
for(i = 0;i<family.length; i++){
    console.log(family[i].name);
}



// Our person constructor
function Person (name, age) {
    this.name = name;
    this.age = age;
}

// We can make a function which takes persons as arguments
// This one computes the difference in ages between two people
var ageDifference = function(person1, person2) {
    return person1.age - person2.age;
};

// Make a new function, olderAge, to return the age of
// the older of two people
var olderAge = function(person1, person2){
    return person1.age > person2.age ? person1.age : person2.age;
}

// Let's bring back alice and billy to test our new function
var alice = new Person("Alice", 30);
var billy = new Person("Billy", 25);

console.log("The older person is "+olderAge(alice, billy));




var spencer = {
  age: 22,
  country: "United States"
};

// make spencer2 here with constructor notation
var spencer2 = new Object();
spencer2.age = 22;
spencer2.country = "United States";




var snoopy = new Object();
snoopy.species = "beagle";
snoopy.age = 10;

// save Snoopy's age and species into variables
// use dot notation for snoopy's species
var species = snoopy.species;
    
// use bracket notation for snoopy's age
var age = snoopy["age"];




function Circle (radius) {
    this.radius = radius;
    this.area = function () {
        return Math.PI * this.radius * this.radius;
        
    };
    // define a perimeter method here
    this.perimeter = function(){
        return 2 * Math.PI * this.radius;
    }
};




// 3 lines required to make the iliad
var harry_potter = new Object();
harry_potter.length = 350;
harry_potter.author = "J.K. Rowling";

// A custom constructor for book
function Book (length, author) {
    this.length = length;
    this.author = author;
}

// Use our new constructor to make the_hobbit in one line
var the_hobbit = new Book(320, "J.R.R. Tolkien")




var bob = {
    firstName: "Bob",
    lastName: "Jones",
    
    phoneNumber: "(650) 777 - 777",
    email: "bob.jones@example.com"
};

console.log(bob.firstName);
console.log(bob.lastName);
console.log(bob.email);




function Person (
    firstName, 
    lastName, 
    phoneNumber, 
    email){
    this.firstName = firstName;
    this.lastName = lastName;
    this.phoneNumber = phoneNumber;
    this.email = email;
}
var bob  = new Person("Bob", "Jones", "(650) 777 - 7777", "bob.jones@example.com");
var mary = new Person("Mary", "Johnson", "(650) 888 - 8888", "mary.johnson@example.com");
var contacts = [bob, mary];
console.log(contacts[1].phoneNumber);
// printPerson added here
var printPerson = function(person){
    console.log(person.firstName + ' ' + person.lastName);
}
printPerson(contacts[0]);
printPerson(contacts[1]);
function list(){
    var length = contacts.length;
    for(i = 0; i < length; i++){
        printPerson(contacts[i]);
    }
}
list();

function search(lastName){
    var length = contacts.length;
    for(i = 0; i < length; i++){
        if (contacts[i].lastName === lastName){
            printPerson(contacts[i]);
        }
    }
}
search("Jones");
function add(
    firstName,
    lastName,
    email,
    telephone
    ){
    var new_contact = {
        firstName: firstName,
        lastName: lastName,    
        phoneNumber: telephone,
        email: email
    };
    var i = contacts.length;
    contacts[i] = new_contact;
    console.log(contacts[i].email);
}
firstName = prompt("?");
lastName = prompt("?");
email = prompt("?");
telephone = prompt("?");
add(    
    firstName,
    lastName,
    email,
    telephone
);


var james = {
    job: "programmer",
    married: false,
    sayJob: function() {
        // complete this method
        console.log("Hi, I work as a " + this.job)        
    }
};

// james' first job
james.sayJob();

// change james' job to "super programmer" here
james.job = "super programmer";

// james' second job
james.sayJob();

james.speak("great");
james.speak("just okay");

// set to the first property name of "james"
var aProperty = "job";

// print the value of the first property of "james" 
// using the variable "aProperty"
console.log(james[aProperty])

function Person(job, married) {
    this.job = job;
    this.married = married;
    this.speak = function(){
        console.log("Hello!");
    }    
}

// create a "gabby" object using the Person constructor!
var gabby = new Person("student", true);