# 1
# two equal Gaussians.. result sigma will be 
# > smaller
# larger
# same



# 2
# two exactly equal Gaussians - sigma will be .5*old_sigma


# 3
# calculate Mu and Sigma for heavy Gaussisan? no


# 4
# dimensions of state vector? 36


# 5
# x_with_dot  = x_
# x'  = x + x_*dt
# x_' = x_

# to get from matrix (x) to matrix (x')
#                    (x_)          (x_'),
# with wich state transition matrix F 
# a1 a2
# b1 b2

# shoud be multiplied initial matrix?
# if we want
# to have a1*x + a2*x_ be same as
#            x + x_*dt,
# and     b1*x + b2*x_ be same as
#                   x_,
# then
# a1 a2
# b1 b2 should be:

# 1 dt
# 0 1

# similarly,
# if we want translate matrix
# x
# y
# x.
# y.

# to

# x'
# y'
# x.'
# y.'
# where
# x'  = x + x.*dt
# y'  = y + y.*dt
# x.' = x.
# y.' = y.
# and by 
# a1 a2 a3 a4
# b1 b2 b3 b4
# c1 c2 c3 c4
# d1 d2 d3 d4
# we got
# x'  = a1*x + a2*y + a3*x. + a4*y.
# y'  = b1*x + b2*y + b3*x. + b4*y.
# x.' = c1*x + c2*y + c3*x. + c4*y.
# y.' = d1*x + d2*y + d3*x. + d4*y.

# that means we want:
# x'  = 1*x + 0*y + dt*x. + 0*y.
# y'  = 0*x + 1*y +  0*x. + dt*y.
# x.' = 0*x + 0*y +  1*x. + 0*y.
# y.' = 0*x + 0*y +  0*x. + 1*y.
# F matrix:
# t = dt
# 1 0 t 0
# 0 1 0 t
# 0 0 1 0
# 0 0 0 1


# 6
