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
# sigma^2 - larger for larger distribution
