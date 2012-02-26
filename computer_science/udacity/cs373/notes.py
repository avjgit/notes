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
#Program a function that returns a new distribution 
#q, shifted to the right by U units. If U=0, q should 
#be the same as p.

#Modify the move function to accommodate the added 
#probabilities of overshooting or undershooting 
#the intended destination.

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        q.append(
            p[(i-(U-1))%len(p)]*pUndershoot +
            p[(i-U)    %len(p)]*pExact +
            p[(i-(U+1))%len(p)]*pOvershoot
        )
    return q
    

print move(p, 1)



# Inexact Motion 1 - Question  
initial = 0 1 0 0 0
movement U = 2
p(x[i+2] | x[i]) = .8
p(x[i+1] | x[i]) = .1
p(x[i+3] | x[i]) = .1

after movement = 0 0 .1 .8 .1

# Inexact Motion 2 - Question  
initial = 0 .5 0 .5 0
after movement, with certain move = .5  0  0   .5  0

probability1 of movement =                 .1  .8  .1
probability2 of movement =          .8 .1  0   0   .1

result of probability1 =             0  0  .05 .4 .05
result of probability2 =            .4 .05 0   0  .05

result total=                       .4 .05 .05 .04 .1 = 1

# Inexact Motion 3 - Question  
init .2  .2  .2  .2  .2
1        .02 .16 .02
2            .02 .16 .02
3    .02         .02 .16 
4    .16 .02         .02
5    .02 .16 .02
sum  .2  .2  .2   .2 .2  :)

# Inexact Move Function - Question  
(above)

# Limit Distribution Quiz - Question  
if from 1 0 0 0 0 
there are many U = 1,
then posterior limit distribution is
.2 .2 .2. 2. 2

# Move Twice - Question  
#Write code that makes the robot move twice and then prints 
#out the resulting distribution, starting with the initial 
#distribution p = [0, 1, 0, 0, 0]

p=[0, 1, 0, 0, 0]
world=['green', 'red', 'red', 'green', 'green']
measurements = ['red', 'green']
pHit = 0.6
pMiss = 0.2
pExact = 0.8
pOvershoot = 0.1
pUndershoot = 0.1

def sense(p, Z):
    q=[]
    for i in range(len(p)):
        hit = (Z == world[i])
        q.append(p[i] * (hit * pHit + (1-hit) * pMiss))
    s = sum(q)
    for i in range(len(q)):
        q[i] = q[i] / s
    return q

def move(p, U):
    q = []
    for i in range(len(p)):
        s = pExact * p[(i-U) % len(p)]
        s = s + pOvershoot * p[(i-U-1) % len(p)]
        s = s + pUndershoot * p[(i-U+1) % len(p)]
        q.append(s)
    return q


# Move 1000 - Question  
# for i in range(1000):
# p = move(p,1)

# Sense And Move - Question  
for i in range(len(measurements)):
    p = sense(p, measurements[i])
    p = move(p, motions[i])
    
print p









# Sense And Move 2 - Question  


# Localization Summary  


# Formal Definition Of Probability 1 - Question  


# Formal Definition Of Probability 2 - Question  


# Formal Definition Of Probability 3 - Question  


# Bayes Rule  


# Cancer Test - Question  
p(c) = 0.001
p(>c)= 0.999

p(positive/ C) = .8
p(positive/>C) = .1

p(C/ positive)?

ok, if test was positive, then could be
.8 of .001 real cancer = .0008, or
.1 of .999 healthy     = .0999
that means, of .1079,
.0008 is  0.8%
.0999 is 99.2%

# Theorem Of Total Probability  


# Coin Flip Quiz - Question  


# Two Coin Quiz - Question  
fair coin has P(heads) = .5
loaded coin's P(heads) = .1

heads observed

P(fair)? = 0.5*0.5 - 0.5*0.1 = 0.5*(.05-0.1) = .5*.4 = .2

correct:

P(F|H) = P(H|F) * P(F) = .5 * .5 = .25 = 25/30 = 5/6 = .8(3)
P(N|H) = P(H|N) * P(N) = .1 * .5 = .05
                                   ---
                                   .30

P(A|B) = (P(B|A) P(A)) / P(B)
http://ru.wikipedia.org/wiki/Теорема_Байеса

P(A)   - вероятность гипотезы А, априорная
Р(А|B) - вероятность гипотезы А, при наступлении события В (апостериорная)
P(B|A) - вероятность события В, при истинности гипотезы А
P(B)   - полноая вероятность наступления события В

Пример:
вероятность брака: 
    у рабочего 1 р1 = .9,
    у рабочего 2 р2 = .5,
    у рабочего 3 р3 = .2
изговили деталей:
    рабочий 1: 800
    рабочий 2: 600
    рабочий 3: 900
Случайная деталь оказалась бракованной.
Какова вероятность, что изготовил рабочий 3?

Р(раб3 | брак) 
= (Р(брак | раб3) * Р(раб))            / Р(брак)
= (            .2 * 900/(800+600+900)) / (16/30)
= (            .2 * 9  /23)  / (16/30)
= (           2/10 * 9 /23)  / (16/30)
= (           2    * 9 /230) / ( 8/15)
=                   18 /230  /   8/15
=                   18 /230  *  15/8
=                   18 * 15  / 230  * 8
= (6 * 3 * 5 * 3) / (23 * 10 * 8)
= (6 * 3 * 5 * 3) / (23 * 2 * 5 * 8)
= (6 * 3 * 3) / (23 * 2 * 8)
= (2 * 3 * 3 * 3) / (23 * 2 * 8)
= (3 * 3 * 3) / (23 * 8)
= 27/ 184
= 14.67%


http://simple.wikipedia.org/wiki/Bayes%27_theorem

There is a 40% chance of it raining on Sunday. 
If it rains on Sunday, there is a 10% chance it will rain on Monday. 
If it didn't rain on Sunday, there's an 80% chance it will rain on Monday.
It rained on Monday. What is the probability it rained on Sunday?


P(rained on Sunday? | it rained on Monday) = 
P(rS | rM) = P(rM | rS) * P (rS) / P (rM)
 = .1 * .4 / (.4*.1 + .6*.8)
 = .04 / (.04 + .48)
 = .04 / .52
 = 4/52 = 2/26 = 1/13

 Intuitive Explanation
* We know that it rained on Monday. Therefore, the total probability is P(B).
* The probability is rained on Sunday is P(A).
* The probability it rained on Monday, given that it rained on Sunday is P(B|A).
* The probability of raining on Sunday AND raining Monday is P(A)*P(B|A).
* Therefore, the total probability of it having rained on Sunday, given that it rained on Monday,
 is the chance of it raining on Sunday multiplied by the chance of it raining on Monday, given that it rained on Sunday, 
 divided by the total chance of it having rained on Monday.
 

http://en.wikipedia.org/wiki/Bayes'_theorem

An entomologist spots what might be a rare subspecies of beetle, due to the pattern on its back. 
In the rare subspecies, 98% have the pattern. 
In the common subspecies, 5% have the pattern. 
The rare subspecies accounts for only 0.1% of the population. 
How likely is the beetle to be rare?
 
P(rare | pattern) 
= P(pattern | rare) * P (rare) / P (pattern) 
= P(pattern | rare) * P (rare) / (98% * .1%  + 5% * 99.9%)
= 98% * .1%                    / (98% * .1%  + 5% * 99.9%)
= .98 * .001                   / (.98 * .001 + .05 * .999)
= .00098                       / (.00098     + .05 * .999)
= 1.9%



Suppose a drug test is 99% sensitive and 99% specific. 
That is, the test will produce 99% true positive and 99% true negative results. 
Suppose that 0.5% of people are users of the drug. 
If an individual tests positive, what is the probability they are a user?

P(user | +) 
= P(+ | user) * P(user) / P(+)
= .99         * .005    / (.99*.005 + .01*995)
= .495% / 1.49% = 33%




# Conclusion  


# HOMEWORK 1
1
p(x) = 0.2
p(x')?


p(x) = 0.2
p(y) = 0.2
x and y are independent
p(x, y)?

p(x) = .2
p(y|x)  = .6
p(y|x') = .6
p(y)?


2

3

4