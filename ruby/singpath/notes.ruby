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
def doublefactorial(x)
    if (x.is_a? String) or 
       (x.is_a? Float)
        return 'TypeError: unsupported type'
    end  
    # this check didn't worked    
    # if (x < 0)
        # return 'OverflowError: math range error'
    # end   
    if x > 1
        x * doublefactorial(x-2)
    elsif x >= 0 
        1
    else
        return 'OverflowError: math range error'
    end
end

08: 
# Ackermann Function
# The Ackermann function ack(m,n), is defined recursively depending on the value of m and n:
 # if m = 0 then n+1 
 # if m > 0 and n = 0 then ack(m-1,1) 
 # if m > 0 and n > 0 then ack(m-1,ack(m,n-1)) 
def ack(m, n)
  if m > 0
    if n > 0 
      ack(m-1, ack(m,n-1))
    elsif n==0
      ack(m-1, 1)
    end
  elsif m == 0
    return n+1
  end
end

09: 
def is_palindrome(word)
  
  if word.length < 2
    return true
  end
  
  return (word[0] == word[word.length-1]) && is_palindrome(word[1..word.length-2])
    
end

10: 
# Greatest Common Factor
# The greatest common divisor (GCD) of a and b is the largest number that divides both of them with no remainder.
# One way to find the GCD of two numbers is Euclid’s algorithm, which is based on the observation that if r is the remainder when a is divided by b, then gcd(a,b) = gcd(b, r). As a base case, we can consider gcd(a,0) = a.
def gcd(a, b)
    if a%b == 0 or b== 0
      return b
    end
    gcd(b, a%b)
end

11:
# A number, a, is a positive integer power of b if it is divisible by b and a/b is a power of b. 
# Write a function called is_power that takes parameters a and b and returns True if a is a positive integer power of b. 
def is_power(a, b)
    if (a == b)
      return true
    else
      return a%b==0 && is_power(a/b, b)
    end
end

------------------------------ level 06 - 00/18 - Iteration
01: 
def sum(n)
  total = 0
  i = 1
  while i<= n
    total += i
    i += 1
  end
  return total
end

02: 
def factorial(n)
    total = 1
    while n > 1
        total = total * n
        n -= 1
    end
    total
end

03: 
def sum(a, b)
    total = 0
    while a <= b
        total += a
        a += 1
    end
    return total
end

04:
# step doesn't work with floats
# def sum(a, b, step)
    # (a..b).step(step) do |n|
        # total += n
    # end
    # return total
# end 
def sum(a, b, step)
    total = 0
    while a <= b
        total += a
        a += step
    end
    return total
end

05: 
def sum_squares(n)
    total = 0
    for i in (1..n)
        total += i**2
    end
    return total
end

06: 
def sum_roots(n)
    total = 0
    for i in (1..n)
        total += Math.sqrt(i)
    end
    return total
end

07: 
def sum_cubes(a, b)
    total = 0
    for i in (a..b)
        total += i**3
    end
    return total
end

08: 
def sum_powers(a, b, power)
    total = 0
    for i in (a..b)
        total += i**power
    end
    return total
end

09: 
def product(a, b, step)
    total = 1
    (a..b).step(step) do |n|
        total *= n
    end
    return total
end

10: 
def sum_squares(numbers)
  total = 0
  for i in numbers do
    total += i**2
  end
  total
end

11: 
def count_evens(numbers)
    count = 0
    for number in numbers
        if number%2 == 0
            count += 1
        end
    end
    count
end

12: 
# Return the sum of the numbers in a list, 
# except ignore sections of numbers starting with a 6 and extending to the next 7 
# (every 6 will be followed by at least one 7). 
# Return 0 for an empty list.

# I assume sections from 6 to nearest 7
def sum67(numbers)
  total = 0
  add = true
  for n in numbers
    
    if n == 6
      add = false
    end
    
    if add
      total += n
    end
    
    if n == 7
      add = true
    end
    
  end
  total
end

13: 
def is_prime(nr)
  prime = true
  #ok, for positive inegers only
  if nr > 1 
    for x in 2..nr-1 do
      if (nr%x == 0)
        prime = false 
      end
    end
  else
    prime = false
  end  
  prime
end

14: 
# A perfect number is a number whose factors sum to itself.
# For example, the factors of 6 are 1, 2, and 3. 1+2+3=6.
# The factors of 28 are 1+2+4+7+14=28.
def is_perfect(nr)
  factors = Array.new
  for i in 1..nr-1 do
    if nr%i ==0 
      # puts 'factor is ' + i.to_s
      factors << i
    end
  end
  sum = 0  
  factors.each do |i|
    # print 'sum ' + sum.to_s + ' + ' + i.to_s
    sum += i
    # puts ' = ' + sum.to_s
  end
  sum
  return sum == nr ? true : false
end
 


15: 
=begin
Determinant
Create a function that calculates the determinant of a given square matrix.
In this problem, we use nested lists to represent matrices, such as
[[6,3],
[4,3]]
or
[[ 2,2,-3],
[-1,1, 3],
[ 2,0,-1]]
To calculate the determinant, there is two properties that might be useful:
1. If a matrix is obtained from another matrix by adding a multiple of a row to another, then they have the same determinant.
2. The determinant of an upper triangular matrix is the product of its diagonal entries, like
Determinant(
[[a,b,c],
[0,d,e],
[0,0, f]])
==a*d*f
More about determinant:
http://www.wikipedia.org/wiki/Determinant
http://mathworld.wolfram.com/Determinant.html
=end
def Determinant(m)
  if m.length == 1
    m[0][0]
  elsif m.length == 2
    m[0][0] * m[1][1] -
    m[0][1] * m[1][0]
  else
    determinant = 0
    size = m.length-1
    for minor in 0..size do
      submatrix = Array.new
      for j in 1..size do      
        submatrix[j-1] = Array.new
        for k in 0..size do
          if k != minor
            submatrix[j-1] << m[j][k]
          end
        end
      end
      determinant += (-1)**minor * m[0][minor] * Determinant(submatrix)
    end
    determinant
  end
end

16: == 15
17: == 15


18: 
def every_second(input)
    result = ''
    for i in 0..input.length do
        if i%2 == 1
            result += input[i].chr
        end
    end
    result
end

# a problem
# Switch values between two variables, without introducing third one, and return the second.
def switch(a, b)
    a = a + b
    b = a - b
    return b
end
------------------------------ level 07 - 00/21 - Strings
01: 
def character(string, nth)
    string[nth].chr
end

02: 
def hello(name)
    'Hello ' + name + '!'
end

03: 
def middle(string)
    string[1..(string.length-2)]
end

04: 
def search(string, char)
    result = string.index(char)
    result.nil? ? -1 : result
end

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