------------------------------ level 01 - 00/10 - The way of SingPath
04: oops=713
05: age = 7
06: spam = 'anxious'
07: name = 4.27; pigs = 'can fly'
08: alpha = 'abcdefghijklmnopqrstuvwxyz'; pi = 3.14159265 
09: quest = 'To seek the Holy Grail.'; airspeed = 43
10: perfect = (4+3)
------------------------------ level 02 - 00/11 - Variables, keywords, and statements
01: spam = 'shrubbery'; age = 37; pi = 3.1415
02: spam = 'spam'
03: count = 1
04: spam = 1000.0
05: 
a = 1
b = 2
total  = a + b

06: 
days_in_a_year = 365
hours_in_a_day = 24
minutes_in_a_hour = 60
seconds_in_a_minute = 60
seconds_in_a_year = days_in_a_year * hours_in_a_day * minutes_in_a_hour * seconds_in_a_minute

07: rice = 2**63
08: 
inches = 69.0
foot_inches = 12
feet = inches/ foot_inches

09: 
spam = 'spam'
eggs = 'eggs'
breakfast = spam + eggs

10: 
spam = 'spam'
times = 57
email = spam*times

11: 
#global = 5
#slip@slide = 5
dog_bone = 5
pig8slop = 5
#class = 5

------------------------------ level 03 - 00/15 - Functions
01: 
def square(x) 
  x*x
end

02: 
def increment (input)
    input + 1
end    

03: 
def product(nr1, nr2)
    nr1*nr2
end

04: 
def sum(a,b)
    a+b
end

05: 
def double_word(word)
    word*2
end    

06: 
def repeat_word(word, times)
    word*times
end    

07: 
def circle_area(radius)
    Math::PI * radius**2
end

08: 
def radian(degrees)
    degrees * Math::PI / 180.0
end    

09: 
def cosine(degrees)
    radians = degrees * Math::PI/180
    Math::cos(radians)
end    

10: 
def add_one(num)
  num+1
end

11: 
def difference(x,y)
    x - y
end    

12: 
def repeat(word)
    word * word.length()
end

13: 
def right_justify(s)
    length = 40
    add_spaces = length - s.length()
    ' ' * add_spaces + s
end

14: 
Function Caller
In many ways functions can be treated in the same way as variables. They can even be passed as arguments into another function. 
For this problem, you need to create a function called double_result() which takes two arguments. The first argument is a function and the second is a value. Your function needs to call the function that is passed to it, passing the value as an argument. Double the result and return that value.
In Ruby, you execute a passed in function by sending other parameters to it. 

def double_result(f,x)
  #send(f,x)*2 #didn't worked
  send(f,x) + send(f,x)
end

def repeat_word(input)
    input*2
end

15: 
def last(num)
    num%10
end

------------------------------ level 04 - 00/17 - Conditionals
01: 
def quotient(a, b)
    a/b
end

02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


11: 


12: 


13: 


14: 


15: 


16: 


17: 


------------------------------ level 05 - 00/11 - Recursion
01: 


02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


11: 


------------------------------ level 06 - 00/18 - Iteration
01: 


02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


11: 


12: 


13: 


14: 


15: 


16: 


17: 


18: 


------------------------------ level 07 - 00/21 - Strings
01: 


02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


11: 


12: 


13: 


14: 


15: 


16: 


17: 


18: 


19: 


20: 


21: 


------------------------------ level 08 - 00/13 - Arrays
01: 


02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


11: 


12: 


13: 


------------------------------ level 09 - 00/10 - Hashes
01: 


02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


------------------------------ level 10 - 00/10 - Tuples
01: 


02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


------------------------------ level 11 - 00/15 - Classes & Objects
01: 


02: 


03: 


04: 


05: 


06: 


07: 


08: 


09: 


10: 


11: 


12: 


13: 


14: 


15: 