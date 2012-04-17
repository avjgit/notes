domain: poker
    hand
    card
    rank
    suit

expected functions:
    poker(hands) -> besthand

combinations:
    n of a kind (n of same of rank)
    straight (sequence)
    flush (same suit)

# -----------
# User Instructions
# 
# Modify the poker() function to return the best hand 
# according to the hand_rank() function. Since we have
# not yet written hand_rank(), clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 
#

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(#enter your code here. Your return should call max())

def hand_rank(hand):
    return None # we will be changing this later.    