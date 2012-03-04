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
	
	quote_start = page.find('"', start_link)
	quote_end   = page.find('"', quote_start+1)
	
	url = page[quote_start+1 : quote_end]
	return url, end_quote
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
# More Friends - Question
# Or
# Biggest - Question
# While Loops - Question
# While Loops 2 - Question
# Print Numbers - Question
# Factorial - Question
# Break - Question
# Multiple Assignment
# Multiple Assignment - Question
# No Links - Question
# Print All Links - Question