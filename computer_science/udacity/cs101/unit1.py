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

start_link = page.find('<a href=')
quote_start = page.find('"', start_link)
quote_end   = page.find('"', quote_start+1)
url = page[quote_start+1 : quote_end]	