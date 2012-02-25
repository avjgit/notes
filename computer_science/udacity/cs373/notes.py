# ----------------- probability
# normalized = if sum of probabilities is 1
# convolution = funciton overlapping
# sample space = set of all possible outcomes

# P(X|Z) = probability of event X, given Z
# P(Heads | Normal coin) = 1/2
# P(Heads | Coin-with-two-heads) = 1

# Bayes' Rule
# "what is the probability that the coin is normal, given that it came up heads?"
# P(X|Z) = (P(Z|X) P(X)) / P(Z)
# P(Normal coin | Heads) = (P(Heads | Normal coin) P(Normal coin)) / P(Heads)
# P(Normal coin | Heads) = (1/2 * 1/2) / 1/2 = 1/4 / 1/2 = 1/2??

# Total Probability Theorem = P of event occuring is sum of probabilities of all possible ways it can occur

# CS373: Programming a Robotic Car  
# Description:   
  
## UNIT1  
# Introduction  
# Localization  
# Total Probability  
# Uniform Probability Quiz - Question  
p = 0.2
# Uniform Distribution - Question  
p = [0.2, 0.2, 0.2, 0.2, 0.2]
# Generalized Uniform Distribution - Question  
    #Modify your code to create probability vectors, p, of arbitrary 
    #size, n. Use n=5 to verify that your new solution matches 
    #the previous one.

    p=[]
    n=5

    for i in range(n):
        p.append(1./n)

    print p
# Probability After Sense - Question  
# multily by .6 or .2
# change of the beliefs after measurement
# why sum is not 1 anymore?
.04 .12 .12 .04 .04

# Compute Sum - Question  
.36

# Normalize Distribution - Question  
ok
1/9 1/3 1/3 1/9 /9

# Phit And Pmiss - Question  
#Write a code that outputs p after multiplying each entry 
#by pHit or pMiss at the appropriate places. Remember that
#the red cells 1 and 2 are hits and the other green cells
#are misses


p=[0.2,0.2,0.2,0.2,0.2]
pHit = 0.6
pMiss = 0.2

#Enter code here
hitCells = [1, 2]
for i in range(len(p)):
    if i in hitCells:
        multiplier = pHit
    else:
        multiplier = pMiss
        
    p[i] = p[i] * multiplier
print sum(p)

# Sum Of Probabilities - Question  


# Sense Function - Question  
#Modify the code below so that the function sense, which 
#takes p and Z as inputs, will output the NON-normalized 
#probability distribution, q, after multiplying the entries 
#in p by pHit or pMiss according to the color in the 
#corresponding cell in world.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    #
    #ADD YOUR CODE HERE
	#
    q = []
    for i in range(len(world)):
        if world[i] == Z:
            q.append(pHit * p[i])
        else:
            q.append(pMiss * p[i])
    
    return q

print sense(p,Z)

# Normalized Sense Function - Question  
#Modify your code so that it normalizes the output for 
#the function sense. This means that the entries in q 
#should sum to one.


p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
Z = 'red'
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    sumq = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / sumq
    return q
print sense(p,Z)


# Test Sense Function - Question  


# Multiple Measurements - Question  
#Modify the code so that it updates the probability twice
#and gives the posterior distribution after both 
#measurements are incorporated. Make sure that your code 
#allows for any sequence of measurement of any length.

p=[0.2, 0.2, 0.2, 0.2, 0.2]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q
#
#ADD YOUR CODE HERE
#
for m in measurements:
    p = sense(p, m)
    
print p



# Exact Motion - Question  
# if P was (1/..)
# /9 /3 /3 /9 /9

# then, after movement, it is
# /9 /9 /3 /3 /9 !

# Move Function - Question  


# Inexact Motion 1 - Question  


# Inexact Motion 2 - Question  


# Inexact Motion 3 - Question  


# Inexact Move Function - Question  


# Limit Distribution Quiz - Question  


# Move Twice - Question  


# Move 1000 - Question  


# Sense And Move - Question  


# Sense And Move 2 - Question  


# Localization Summary  


# Formal Definition Of Probability 1 - Question  


# Formal Definition Of Probability 2 - Question  


# Formal Definition Of Probability 3 - Question  


# Bayes Rule  


# Cancer Test - Question  


# Theorem Of Total Probability  


# Coin Flip Quiz - Question  


# Two Coin Quiz - Question  


# Conclusion  


# HOMEWORK 1