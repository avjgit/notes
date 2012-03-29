# 01 Infinite Power
# 02 Long Words - Question
# 03 Counter
# 04 Counter Quiz - Question
# 05 Expanding Our Grammar - Question
# 06 Recursive Definitions
# 07 Ancestors - Question
# 08 Recursive Procedures
# 09 Recursive Factorial - Question
#Define a procedure, factorial, that takes a natural number as its input, and
#outputs the number of ways to arrange the input number of itmes.

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)




#print factorial(0)
#>>> 1
#print factorial(5)
#>>> 120
#print factorial(10)
#>>> 3628800


# 10 Palindromes - Question
#Define a procedure is_palindrome, that takes as input a string, and returns a
#Boolean indicating if the input string is a palindrome.

#Base Case: '' => True
#Recursive Case: if first and last characters don't match => False
#if they do match, is middle palindrome?

def is_palindrome(s):
    return (s == '') or (s[0] == s[-1] and is_palindrome(s[1:-2]))

    
print is_palindrome('')
#>>> True
print is_palindrome('abab')
#>>> False
print is_palindrome('abba')
#>>> True


# 11 Recursive Vs Iterative
# 12 Bunnies - Question
#Define a procedure, fibonacci, that takes a natural number as its input, and
#returns the value of that fibonacci number.

#Two Base Cases:
#    fibonacci(0) => 0
#    fibonacci(1) => 1

#Recursive Case:
#    n > 1 : fibonacci(n) => fibonacci(n-1) + fibonacci(n-2)

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610

# 13 Divide And Be Conquered
# 14 Counting Calls - Question
# 15 Faster Fibonacci - Question

Recoursion is very expensive

#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    f_2 = 0
    f_1 = 1
    for i in range(2,n+1):
        sum = f_1 + f_2
        f_2 = f_1
        f_1 = sum
    return sum

def fibonacci_small(n):
    current = 0
    next = 1
    for i in range(0, n):
        current, next = next, current + next
    return current

            


print fibonacci(36)
#>>> 14930352

# 16 Ranking Web Pages
# 17 Popularity
# 18 Good Definitions - Question
# 19 Circular Definitions - Question
# 20 Relaxation - Question
# 21 Page Rank
# 22 Altavista - Question
# 23 Urank
# 24 Implementing Urank - Question
# 25 Computing Page Rank
# 26 Formal Calculations
# 27 Computer Ranks
# 28 Finishing Urank - Question
# 29 Search Engine
