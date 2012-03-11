# 1. open classes, metaprogramming, duck typing


# a) [ELLS ex. 3.11] Extend the currency-conversion example from lecture so that you can write
# 5.dollars.in(:euros)
# 10.euros.in(:rupees)
# etc.
# ● You should support the currencies 'dollars', 'euros', 'rupees' , 'yen' where the
# conversions are: rupees to dollars, multiply by 0.019; yen to dollars, multiply by 0.013;
# euro to dollars, multiply by 1.292.
# ● Both the singular and plural forms of each currency should be acceptable, e.g.
# 1.dollar.in(:rupees) and 10.rupees.in(:euro) should work.
# You can use the code shown in lecture as a starting point if you wish; it is at http://pastebin.com/
# agjb5qBF

class Numeric
  @@currencies = {'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019, 'dollar' => 1.0, 'lat' => 2.0}
    # ● Both the singular and plural forms of each currency should be acceptable, e.g.
    # 1.dollar.in(:rupees) and 10.rupees.in(:euro) should work.
  def method_missing(method_id)
    singular_currency = method_id.to_s.gsub( /s$/, '')
    if @@currencies.has_key?(singular_currency)
      self * @@currencies[singular_currency]
    else
      super
    end
  end
  # first, convert everything to dollars
  def in (currency)
    @dollars = self * @@currencies['dollar']
    
    # then convert dollars to currency needed
    # todo: how to get rid of repetition?
    singular_currency = currency.to_s.gsub( /s$/, '')
    if @@currencies.has_key?(singular_currency)
      @dollars / @@currencies[singular_currency]
    else
      super
    end

  end
end

# puts 10.euro.in(:dollars)
# puts 10.dollars.in(:euro)
# puts 12.lats.in
# currencies = {'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019, 'dollar' => 1.0, 'lat' => 2.0}
# puts currencies['yen']

# b) Adapt your solution from HW 1 "palindromes" question so that instead of writing palindrome?
# ("foo") you can write "foo".palindrome? HINT: this should require fewer than 5 lines of code.
class String
    def palindrome?
      self.downcase!
      self.gsub!(/[^a-z]/, '')    #unify case & remove non-letters
      half = self.length/2            #get self length
      part1 = self[0..half-1].reverse
      part2 = self[-half..-1]
      part1 ==  part2           #compare first half to second
    end
end

# c) Adapt your palindrome solution so that it works on Enumerables. That is:
# [1,2,3,2,1].palindrome? # => true
# (It's not necessary for the collection's elements to be palindromes themselves--only that the
# top-level collection be a palindrome.) HINT: this should require fewer than 5 lines of code.
# Although hashes are considered Enumerables, your solution does not need to make sense for
# hashes (though it should not error).
module Enumerable
    def palindrome?
      # self.downcase!
      # self.gsub!(/[^a-z]/, '')    #unify case & remove non-letters

      # half = self.length/2            #get self length
      # part1 = self[0..half-1].reverse
      # part2 = self[-half..-1]
      # part1 ==  part2           #compare first half to second

      storage = []
      self_array = self.to_a
      self_array.map {|x| storage << x}
      storage.reverse == self_array

    end
end

# puts [1, 2, 3, 3, 2, 1].palindrome?
# puts [1, 2, 3, 4, 2, 1].palindrome?

# (1..2).map {|x| puts x}

# a = [1, 2, 3]
# puts a
# puts a.reverse