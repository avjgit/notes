# 5 guys and monkey problem
# 2.3
#Write a function that takes the number of 
#coconuts, n, as an argument and returns the
#number of coconuts after one is given to
#the monkey and one fifth are taken away.
def f(n):
    return (n-1) / 5. * 4

def f6(n):
    for i in range(6):
        if is_int(n):
            n = f(n)
        else:
            break
    return n

def is_int(n):
    return abs(n-int(n)) < 0.0000001
#Write a program that will find the initial number
#of coconuts.    
# Enter code here.    
# i = 0
# n = 0
# while True:
#     i += 1
#     n = f6(float(i))
#     if is_int(n):
#         break
n = 0
found = False
while not found:
    n += 1
    found = is_int(f6(float(n)))

print(n)    

#8
# Kalman filter
#     continuous
#     uni-modal

# Monte Carlo localization
#     discrete
#     multi-modal

# Particle filters
#     continuous
#     multi-modal

#9
# Gaussian can be defined per:
#     mean Monte
#     variance G^2

#10
# sigma^2 
    # - larger for larger distribution
    # - smaller for certain distribution

#12
f(x) = 1/sqr(2*Pi*sigma^2) * e^(-1/2 * (x-M)^2/ sigma^2)
if
    m = 10
    sigma = 2
    x = 8
f(x) = 1/sqr(2*3*4) * e^(-1/2 * (8-10)^2/ 4)
f(x) = 1/sqr(24)    * e^(-1/2 * (-2)^2  / 4)
f(x) = 1/5          * e^(-1/2 *      4  / 4)
f(x) = 0.2          * e^(-1/2 *           1)
f(x) = 0.2          * e^ -1/2
f(x) = 0.2          * .6
f(x) = 1.2

#13
#For this problem, you aren't writing any code.
#Instead, please just change the last argument 
#in f() to maximize the output.

from math import *

def f(mu, sigma2, x):
    return 1/sqrt(2.*pi*sigma2) * exp(-.5*(x-mu)**2 / sigma2)

print f(10.,4.,10.) #Change the 8. to something else!


#14
                convolution     product
measurement                     X
motion          X