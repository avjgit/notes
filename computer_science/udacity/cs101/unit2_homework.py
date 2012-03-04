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