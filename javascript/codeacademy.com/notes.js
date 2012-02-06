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


