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

# Modify the hand_rank function so that it returns the
# correct output for the remaining hand types, which are:
# full house, flush, straight, three of a kind, two pair,
# pair, and high card hands. 
# 
# Do this by completing each return statement below.
#
# You may assume the following behavior of each function:
#
# straight(ranks): returns True if the hand is a straight.
# flush(hand):     returns True if the hand is a flush.
# kind(n, ranks):  returns the first rank that the hand has
#                  exactly n of. For A hand with 4 sevens 
#                  this function would return 7.
# two_pair(ranks): if there is a two pair, this function 
#                  returns their corresponding ranks as a 
#                  tuple. For example, a hand with 2 twos
#                  and 2 fours would cause this function
#                  to return (4, 2).
def hand_rank(hand):

# (ranking, cardid)
# "straight flush, jack high" - (8, 11)
# "four aces, and a queen" - (7, 14, 12)
# "full house, eights over kings" - (6, 8, 13)
# "flush, 10-8" (5, [10, 8, 7, 5, 3])
# "straight, jach high" (4, 11)
# "three sevens" (3, 7, [7, 7, 7, 5, 2])
# "two pairs, jacks and threes" (2, 11, 3, [13, 11, 11, 3, 3])
# "pair of twoos, jack high" (1, 2, [11, 6, 3, 2, 2])
# "nothing" (0, [7, 5, 4, 3, 2])
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(2, ranks), ranks)
    else:                                          # high card
        return (0, ranks)


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
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    
    # Modify the test() function to include three new test cases.
    # These should assert that card_ranks gives the appropriate
    # output for the given straight flush, four of a kind, and
    # full house.
    #
    # For example, calling card_ranks on sf should output  
    # [10, 9, 8, 7, 6]
    assert card_ranks(sf)
    assert card_ranks(fk)
    assert card_ranks(fh)
print test()   

tuple(7, 9, 5) # like immutable set 
(7, 9, 5) > (7, 3, 2) #valid comparison

# -----------
# User Instructions
# 
# Modify the card_ranks() function so that cards with
# rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# are handled correctly. Do this by mapping 'T' to 10, 
# 'J' to 11, etc...

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
    ranks.sort(reverse=True)
    return ranks

print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]

# -----------
# User Instructions
# 
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    for i in range(0, len(ranks)):
        if ranks[i] != ranks[0] + i:
            return false
    return true

def flush(hand):
    "Return True if all the cards have the same suit."
    suite = hand[0]
    for r, s in hand:
        if s != suite:
            return false
    return true
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

print test()