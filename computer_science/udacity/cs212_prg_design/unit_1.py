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

# -----------
# User Instructions
# 
# Modify the test() function to include two new test cases:
# 1) four of a kind (fk) vs. full house (fh) returns fk.
# 2) full house (fh) vs. full house (fh) returns fh.
#
# Since the program is still incomplete, clicking RUN won't do 
# anything, but clicking SUBMIT will let you know if you
# have gotten the problem right. 

def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # => ['6C', '7C', '8C', '9C', 'TC']
    fk = "9D 9H 9S 9C 7D".split() 
    fh = "TD TC TH 7C 7D".split()
    assert poker([sf, fk, fh]) == sf
    
    # Add 2 new assert statements here. The first 
    # should check that when fk plays fh, fk 
    # is the winner. The second should confirm that
    # fh playing against fh returns fh.
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh


    # Add 2 new assert statements here. The first 
    # should assert that when poker is called with a
    # single hand, it returns that hand. The second 
    # should check for the case of 100 hands.
    assert poker([fk]) == fk
    assert poker([fk] * 100) == fk

    # Modify the test() function to include three new test cases.
    # These should assert that hand_rank gives the appropriate
    # output for the given straight flush, four of a kind, and
    # full house.
    #
    # For example, calling hand_rank on sf should output (8, 10)
    assert hand_rank(sf) = (8, 10)
    assert hand_rank(fk) = (7, 9, 7)
    assert hand_rank(fh) = (6, 10, 7)
    
print test()   

tuple(7, 9, 5) # like immutable set 
(7, 9, 5) > (7, 3, 2) #valid comparison

(ranking, cardid)
"straight flush, jack high" - (8, 11)
"four aces, and a queen" - (7, 14, 12)
"full house, eights over kings" - (6, 8, 13)
"flush, 10-8" (5, [10, 8, 7, 5, 3])
"straight, jach high" (4, 11)
"three sevens" (3, 7, [7, 7, 7, 5, 2])
"two pairs, jacks and threes" (2, 11, 3, [13, 11, 11, 3, 3])
"pair of twoos, jack high" (1, 2, [11, 6, 3, 2, 2])
"nothing" (0, [7, 5, 4, 3, 2])