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
                convolution     product     Bayes rule      Total probability
measurement                     X           X
motion          X                                           X

#18 - todo: write formula down?
# cool:) guessed without calculation

#21 - check calculation

#22
# Write a program to update your mean and variance
# when given the mean and variance of your belief
# and the mean and variance of your measurement.
# This program will update the parameters of your
# belief function.

def update(mean1, var1, mean2, var2):
    new_mean = (var2*mean1 + var1*mean2)/(var1 + var2)
    new_var = 1./ (1./var1 + 1./var2)
    return [new_mean, new_var]

print update(10.,8.,13., 2.)


#23 motion update
m_new = m + u
sigma_new = sigma + other_sigma


# Write a program that will predict your new mean
# and variance given the mean and variance of your 
# prior belief and the mean and variance of your 
# motion. 
def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var =  var1  + var2
    return [new_mean, new_var]

#25
# Write a program that will iteratively update and
# predict based on the location measurements 
# and inferred motions shown below. 

def update(mean1, var1, mean2, var2):
    new_mean = (var2 * mean1 + var1 * mean2) / (var1 + var2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

def predict(mean1, var1, mean2, var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sig = 4.
motion_sig = 2.
mu = 0
sig = 10000

#Please print out ONLY the final values of the mean
#and the variance in a list [mu, sig]. 

# Insert code here

print [mu, sig]
