# 5 guys and monkey problem
# 2.3
#Write a function that takes the number of 
#coconuts, n, as an argument and returns the
#number of coconuts after one is given to
#the monkey and one fifth are taken away.
def f(n):
    return (n-1) / 5 * 4

def f6(n):
    for i in range(6):
        n = f(n)
    return n

def is_int(n):
    return abs(n-int(n)) < 0.0000001
#Write a program that will find the initial number
#of coconuts.    
# Enter code here.    

print(f6(96.))