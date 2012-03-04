# 1/7
# Define a procedure, udacify, that takes as 
# input a string, and returns a string that 
# is an uppercase 'U' followed by the input string.
# for example, when we enter

# print udacify('dacians')

# the output should be the string 'Udacians'

# Make sure your procedure has a return statement.

def udacify(input):
    return 'U' + input

# 3/7
# Define a procedure, median, that takes three
# numbers as its inputs, and outputs the median
# of the three numbers.

# Make sure your procedure has a return statement.

def bigger(a,b):
    if a > b:
        return a
    else:
        return b
        
def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    # if a >= b:
    #     if c >= a:
    #         median = a
    #     else:
    #         if b >= c:
    #             median = b
    #         else:
    #             median = c
    # else:
    #     if b >= c:
    #         if c >= a:
    #             median = c
    #         else:
    #             median = a
    #     else:
    #         median = b
    if a == biggest(a, b, c):
        if b >= c:
            median = b
        else:
            median = c
    else:
        if b == biggest(a, b, c):
            if a >= c:
                median = a
            else:
                median = c
        else:
            if a >= b:
                median = a
            else:
                median = b
    return median

# 4/7
# Define a procedure, countdown, that takes a
# positive whole number as its input, and prints 
# out a countdown from that number to 1, 
# followed by Blastoff! 

def countdown(count):
	while count >= 1:
		print count
		count = count - 1
	print "Blastoff!"

# 5/7

  always finishes
  sometimes funs foerever
  unknown

# Loop 1
n = any positive integer
i = 0
while i <= n:
    i = i+1

> always finishes
  sometimes funs foerever
  unknown

# Loop 2
n = any positive integer
i = 1
while True:
    i = i*2
    n = n+1
    if i > n:
        break

> always finishes
  sometimes funs foerever
  unknown

# Loop 3
n = any positive integer
while n != 1:
    if n % 2 == 0: # n is even
        n = n/2
    else:
        n = 3*n + 1


> always finishes
  sometimes funs foerever
  unknown

# 6/7
# Define a procedure, find_last, that takes as input
# two strings, a search string and a target string,
# and outputs the last position in the search string
# where the target string appears, or -1 if there
# are no occurences.
#
# Example: find_last('aaaa', 'a') returns 3

# Make sure your procedure has a return statement.

def find_last():    

# 7/7
#Define a procedure,
#print_multiplication_table,
#that takes as input a positive whole
#number, and prints out a multiplication,
#table showing all the whole number
#multiplications up to and including the
#input number. The order in which the
#equations are printed must match exactly.

#print_multiplication_table(2)
#1 * 1 = 1
#1 * 2 = 2
#2 * 1 = 2
#2 * 2 = 4

def print_mult(i, j):
    print str(i) + ' * ' + str(j) + ' = ' + str(i*j)

def print_multiplication_table(n):
    i = 1
    while i <= n:
        j = 1
        while j <= n:
            print_mult(i, j)
            j += 1
        i += 1