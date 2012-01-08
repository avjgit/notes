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
def remainder(a, b)
    a%b
end

03: 
def equal(a, b)
    a == b        
end

04: 
def sign(x)
  if x==0
      return 0
  elsif x > 0
      return 1
  else 
      return -1
  end
end  

05: 
def love6(a, b)
    if (a == 6) or (b == 6) or ((a + b) == 6) or ((a - b) == 6) or ((b - a) == 6)    
        return true
    else
        return false
    end
end

06: 
def is_triangle(a, b, c)
    if ((a+b) > c) or ((b+c) > a) or ((c+a) > b)
        return true
    else
        return false
    end
end

07: 
def ticket(a, b, c)
    if (a==b) && (b==c) && (c==2)
        return 10
    elsif (a==b) && (b== c)
        return 5
    elsif (a!=b) && (b!=c) && (c!=a)
        return 1
    else
        return 0
    end 
end

08: 
def alarmClock(day, vacation)
    if day == 0 or day == 6
        if vacation 
            return "off"
        else
            return "10:00"
        end
    else
        if vacation
            return "10:00"
        else
            return "7:00"
        end
    end
end

09: 
def in1to10(number, outside)
    if outside
        if number <= 1 or number >= 10
            return true
        else
            return false
        end
    else
        if number >= 1 and number <= 10
            return true
        else
            return false
        end
    end
end

10: 
def date_fashion(you,date)
    if you < 3 or date < 3
        return 0
    elsif you > 7 or date > 7
        return 2
    else
        return 1
    end
end

11: 
def near_ten(number)
    number%10 <= 2 or number%10 >=8
end

12: 
def do_math(num)
    x = num + 2
    return x + 1
end

13: 
def divide_all(x,y,z)
    d = (y/1.0)/z
    return x/d
end

14: 
def lone_sum(a, b, c)
    if a == b && b == c
        return 0
    elsif a == b
        return c
    elsif b == c
        return a
    elsif c == a
        return b
    else
        return a + b + c
    end 
end

15: 
/*
return if it's possible to make GOAL long wall
of BIG many big bricks, 5 inches long, 
and SMALL many small ones, 1 inche long 
*/
def make_bricks(small, big, goal)
    # we'll use enought 1-sizes brickes to fill the gap
    # to find out, how big the gap is:
    if (big*5) > goal        
        (goal%5) <= small
    else
        (goal - big*5) <= small
    end     
end

16: 
def is_odd(integer)
    integer%2 > 0
end

17: 
/*
You are the programmer for an elevator installation company. 
You need to create a program that will select the best elevator to be used 
when someone calls the elevator to their floor. 
For this program you will be worried only about sending the closest elevator. 
You don't need to worry about whether the elevator is already moving or not.
Create a function elevator that takes three parameters: alevel, blevel, and button. 
You should return the string 'a', 'b', or 'either'
 to represent which lift is closer to the button press.
*/
def elevator(alevel, blevel, button)
    adist = (alevel - button).abs
    bdist = (blevel - button).abs
    if adist < bdist
        return 'a'
    elsif bdist < adist
        return 'b'
    else
        return 'either'
    end 
end

------------------------------ level 05 - 00/11 - Recursion
01: 
def compare(x, y)
    if x > y
        return 1
    elsif x < y
        return -1
    else
        return 0
    end
end

02: 
def is_divisible(a, b)
    a%b == 0
end

03: 
def is_between(a, b, c)
    a <= b && b <= c
end

04: 
# distance between 2 points
def distance(x1, y1, x2, y2)
    Math.sqrt((x2-x1)**2 + (y2-y1)**2)
end

05: 
def factorial(x)
    if x > 0
        x * factorial(x-1)
    else
        1
    end
end

06: 
def fibonacci(order)
  if (order <= 2)
    return 1
  else
    fibonacci(order-1) + 
    fibonacci(order-2)    
  end
end

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