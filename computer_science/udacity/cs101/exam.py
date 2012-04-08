# 01 Grammars
# How many different strings can the following grammar generate, starting from Word?
# Word → udacious
# Word → super Word
# :: I think, infinitely many

# 02 Procedures And If
#Define a procedure, unique, that takes three numbers as its inputs and returns
#the Boolean value True if all three numbers are different. Otherwise, it should
#return the Boolean value False.

def unique(a, b, c):
    return not (a == b or b == c or a == c)


#For example,

# print (unique(1, 2, 3))
#>>> True

# print (unique(1, 0, 1))
#>>> False

# print (unique(7, 7, 7))
#>>> False

# 03 Prefix Removal
#Prefix Removal


#Define a procedure, remove_prefix, that takes as input a string, and returns a
#string that is the part of the string following the first hyphen -. If the input string does
#not contain any hyphen -, remove_prefix should return the full input string.

def remove_prefix(s):
    hyphen = s.find("-")
    return s[hyphen+1:]



#For example,

# print(remove_prefix('super-udacity'))
#>>> 'udacity'

# print(remove_prefix('counter-counter-intelligence'))
#>>> 'counter-intelligence'

# print(remove_prefix('antigravity'))
#>>> 'antigravity'

# 04 Collatz Returns
#Collatz Returns!


#Define a procedure, collatz_steps, that takes as input a positive integer, n, and returns
#the number of steps it takes to reach 1 by following these steps:

#    If n is even, divide it by 2. (You can test for evenness using n % 2 == 0.)
#    If n is odd, replace it with 3n + 1.

def collatz_steps(n):
    steps = 0
    while n > 1:
        steps = steps + 1
        if n%2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return steps


#For example,

print(collatz_steps(1))
#>>> 0

print(collatz_steps(2))
#>>> 1

print(collatz_steps(6))
#>>> 8

print(collatz_steps(101))
#>>> 25

# 05 Cost
# 06 List Explosion
# 07 Reverse Index
# 08 Same Structure
# 09 Reachability
# 10 Spelling Correction
# 11 Multiword Queries