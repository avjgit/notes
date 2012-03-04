# Introduction
page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'

start_link = page.find('<a href=')
quote_start = page.find('"', start_link)
quote_end   = page.find('"', quote_start+1)
url = page[quote_start+1 : quote_end]
print url

page = page[quote_end:]

start_link = page.find('<a href=')
quote_start = page.find('"', start_link)
quote_end   = page.find('"', quote_start+1)
url = page[quote_start+1 : quote_end]
print url



# Motivating Procedures
# Introducing Procedures
# Procedure Code - Question
# Output - Question
# Return Statement - Question
def get_next_target(page):
	start_link = page.find('<a href=')

    if start_link < 0:
        return None, 0
        	
	quote_start = page.find('"', start_link)
	quote_end   = page.find('"', quote_start+1)
	
	url = page[quote_start+1 : quote_end]
	return url, quote_end
# Dave Sebastian And Junior
	cool car
# Using Procedures
def rest_of_string(s):
	return s[1:]
print rest_of_string('audacity')	
# Inc Procedure - Question
# Sum Procedure - Question
# Sum Procedure With A Return Statement - Question
def sum(a, b):
	return a+b
# Square - Question
def square(x):
    return x*x
# Sum Of Three - Question
def sum3(a, b, c):
    return a+b+c
# Abbaize - Question
def abbaize(s1, s2):
	return s1 + s2*2 + s1
# Find Second - Question
def find_second(search, target):
    first  = search.find(target)
    second = search.find(target, first+1)
    return second
# Equality Comparisons - Question
# If Statements - Question
def bigger(a, b):
    if a > b:
        return a
    return b
# Is Friend - Question
def is_friend(name):
    # if name[0] == 'D':
    #     is_friend = True
    # else:
    #     is_friend = False
    return is_friend
# More Friends - Question
def is_friend(name):
    if name[0] == 'D':
        is_friend = True
    else:
        if name[0] == 'N':
            is_friend = True
        else:
            is_friend = False
    return is_friend
# Or
	return True of asdf #=> True
# Biggest - Question
def biggest(a, b, c):
    if a > b:
        if a > c:
            biggest = a
        else:
            biggest = c
    else:
        if b > c:
            biggest = b
        else:
            biggest = c
    return biggest

def biggest(a, b, c):
	# built-in max(a, b, c)
	return bigger(bigger(a, b), c)
	    
# While Loops - Question
i = 0
while i < 10:	#will run 0 to 9
	print i
	i += 1

k = 0
while k != 10: #will run 1 to 10
	k += 1
	print 1
# While Loops 2 - Question
i = 1
while i != 10:	#will run forever
	i = i + 2
	print i
# Print Numbers - Question
# Define a procedure, print_numbers, that takes
# as input a positive whole number, and prints 
# out all the whole numbers from 1 to the input
# number.

# Make sure your procedure prints "upwards", so
# from 1 up to the input number.

def print_numbers(upto):
    i = 1
    while i <= upto:
        print i
        i += 1
# Factorial - Question
def factorial(n):
    factorial = 1
    while n > 1:
        factorial = factorial * n
        n = n-1
    return factorial
# Break - Question
while condition:
	do_code

while True:
	if condition:
		break
	do_code	
# Multiple Assignment
	a, b = 3, 4
	a, b = get_next_target(page)
# Multiple Assignment - Question
	s, t = t, s # swaps valuess
# No Links - Question
print get_next_target('good')
print get_next_target('Not "good" at all')
# Print All Links - Question