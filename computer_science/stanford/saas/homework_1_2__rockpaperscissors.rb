# Part 2: Rock-Paper-Scissors
# In a game of rock-paper-scissors, each player chooses to play Rock (R), Paper (P), 
# or Scissors (S).  The rules are: Rock beats Scissors, Scissors beats Paper, but 
# Paper beats Rock.
# A rock-paper-scissors game is encoded as a list, where the elements are 2-element 
# lists that encode a player’s name and a player’s strategy.
# [ [ "Armando", "P" ], [ "Dave", "S" ] ] 
# # => returns the list ["Dave", "S"] wins since S>P
# (a)  Write a method rps_game_winner that takes a two-element list and behaves 
# as follows:
# - If the number of players is not equal to 2, raise WrongNumberOfPlayersError
# - If either player's strategy is something other than "R", "P" or "S" (case-insensitive), 
# raise NoSuchStrategyError
# - Otherwise, return the name and strategy of the winning player.  If both players use 
# the same strategy, the first player is the winner.
# We'll get you started:
class WrongNumberOfPlayersError < StandardError ; end
class NoSuchStrategyError < StandardError ; end
def rps_game_winner(game)

    raise WrongNumberOfPlayersError unless game.length == 2

    correctStrategies = [:R, :P, :S]

    game.each do |player|
        raise NoSuchStrategyError unless correctStrategies.include?(player[1].upcase.to_sym)
    end

    strategy1 = game[0][1].to_sym
    strategy2 = game[1][1].to_sym

    winner = game[0]

    case strategy1
    when :R
        if strategy2 == :P
            winner = game[1]
        end
    when :P
        if strategy2 == :S
            winner = game[1]
        end
    when :S
        if strategy2 == :R
            winner = game[1]
        end
    end

    winner
end

#tests
# puts rps_game_winner([ [ "Armando", "P" ], [ "Dave", "S" ]] )
# puts rps_game_winner([ [ "Armando", "R" ], [ "Dave", "P" ]] )


# (b) A rock, paper, scissors tournament is encoded as a bracketed array of games -
# that is, each element can be considered its own tournament.
# [
# [
# [ ["Armando", "P"], ["Dave", "S"] ],
# [ ["Richard", "R"],  ["Michael", "S"] ],
# ],
# [ 
# [ ["Allen", "S"], ["Omer", "P"] ],
# [ ["David E.", "R"], ["Richard X.", "P"] ]
# ]
# ]Under this scenario, Dave would beat Armando (S>P), Richard would beat Michael 
# (R>S), and then Dave and Richard would play (Richard wins since R>S); similarly, 
# Allen would beat Omer, David E. would beat Richard X., and Allen and Richard X. 
# would play (Allen wins since S>P); and finally Richard would beat Allen since R>P, 
# that is, continue until there is only a single winner.  Write a method 
# rps_tournament_winner that takes a tournament encoded as a bracketed array 
# and returns the winner (for the above example, it should return [“Richard”, 
# “R”]).  You can assume that the array is well formed (that is, there are 2^n players, 
# and each one participates in exactly one match per round)
def rps_tournament_winner(tournament)
    # puts 'tournament is now '
    # puts tournament
    if tournament[0][0].class == String 
       puts rps_game_winner(tournament) 
    else
        rps_tournament_winner(tournament[0])
    end
end

#tests
rps_tournament_winner [
[
    [ ["Richard", "R"],  ["Michael", "P"] ],
    [ ["Armando", "P"], ["Dave", "P"] ]
],
[ 
[ ["Allen", "S"], ["Omer", "P"] ],
[ ["David E.", "R"], ["Richard X.", "P"] ]
]
]