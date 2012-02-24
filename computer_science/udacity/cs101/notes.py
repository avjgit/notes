# Python reference
# <Name1>,,, <Name2>,,, ... === <Expression1>,,, <Expression2>,,, .

# s, t = t, s   
# would swap the values of sss and ttt so after the assignment statement sss now refers to the previous 
# value of ttt, and ttt refers to the previous value of sss.

# string[number]
# string[-number] - counts from end
# string[start:stop]
# string.find(something)
# string.find(something, start_look_from)

# str(23) = '23'

# Backus-Naur Form (BNF):
# <Nonterminal> -> Terminal
# something_to_define = value

weeks = 7
days_in_week = 7
hours_in_day = 24
min_in_hour = 60
print weeks * days_in_week * hours_in_day * min_in_hour

# Write Python code to print out how far light travels 
# in centimeters in one nanosecond.  Use the variables
# defined below.    

speed_of_light = 299792458   # meters per second
meter = 100                  # one meter is 100 centimeters
nanosecond = 1.0/1000000000  # one billionth of a second

print speed_of_light * meter * nanosecond

Admiral Grace Hopper is cool:)

#Given the variables defined here, write Python 
#code that prints out the distance, in meters, 
#that light travels in one processor cycle. 

speed_of_light = 299792458.0
cycles_per_second = 2700000000.0
print speed_of_light/ cycles_per_second

s = 'audacity'
print 'U' + s[2:]

-- 36:
for any strings and t, and number i,
s.find(t, i) = ?
    s[i:].find(t)
    s.
    
    
# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

# page = contents of a web page
page ='<div id="top_bin"><div id="top_content" class="width960"><div class="udacity float-left"><a href="http://www.xkcd.com">'
tag = '<a href="'
start_link = page.find(tag) 
end_link = page.find('">', start_link)
url = page[start_link+len(tag):end_link]

unit 1 homework
#Write Python code that prints out the number of hours in 7 weeks.
weeks = 7
day_in_week = 7
h_in_day = 24
h_in_week = weeks * day_in_week * h_in_day
print h_in_week

#Write Python code that stores the distance 
#in meters that light travels in one 
#nanosecond in the variable, nanodistance. 

#These variables are defined for you:
speed_of_light = 299800000. #meters per second
nano_per_sec = 1000000000. #1 Billion

#After your code,running
#print nanodistance
#should output 0.2998

#Note that nanodistance must be a decimal number.

#DO NOT USE IMPORT






#ASSIGN nanodistance HERE
nanodistance = speed_of_light/ nano_per_sec
print nanodistance




#Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
#write Python code that prints out udacious
#without using any quote characters in
#your code.

#DO NOT USE IMPORT

print s[:5] + t[-3:]





#Assume text is a variable that
#holds a string. Write Python code
#that prints out the position
#of the second occurrence of 'zip'
#in text, or -1 if it does not occur
#at least twice.

#For example,
#   text = 'all zip files are zipped' -> 18
#   text = 'all zip files are compressed' -> -1

text = "all zip files are zipped" 

#DO NOT USE IMPORT

#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT
start = text.find('zip')
print text.find('zip', start+1)









#Given a variable, x, that stores
#the value of any decimal number,
#write Python code that prints out
#the nearest whole number to x.

#You can assume x is not negative.

# x = 3.14159 -> 3 (not 3.0)
# x = 27.63 -> 28 (not 28.0)

x = 3.14159

#DO NOT USE IMPORT

#ENTER CODE BELOW HERE
#ANY CODE ABOVE WILL CAUSE
#HOMEWORK TO BE GRADED
#INCORRECT
# ok, without any loops, just with strings and serching:)
# idea: let's convert x to string and take part after coma
s = str(x)
decimal_start = s.find('.') + 1
# and check the very first digit after coma is it in range 5..9
# if, yes, number should be rounded up
# but hack is: to round up (+1) the number already before
# and, if no 5..9 as first digit after coma found, then round down
# to be able to solve with techniques learned in this unit

x = x + 1 + s[decimal_start].find('5')
x = x + 1 + s[decimal_start].find('6')
x = x + 1 + s[decimal_start].find('7')
x = x + 1 + s[decimal_start].find('8')
x = x + 1 + s[decimal_start].find('9')

# and now, let's just take part before coma
s = str(x)
comma = s.find('.')
print s[:comma]
