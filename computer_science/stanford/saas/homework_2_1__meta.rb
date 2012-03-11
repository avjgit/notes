# 1. open classes, metaprogramming, duck typing
# description:
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
# lef todo:
# a) [ELLS ex. 3.11] Extend the currency-conversion example from lecture so that you can write
# 5.dollars.in(:euros)
# 10.euros.in(:rupees)
# etc.

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
  def in (#dollars
    )
    self / @@currencies['dollar']
  end
end



puts 5.lats
puts 10.dollar
puts 11.dollars.in
puts 10.yen.in
puts 10.euro.in
puts 10.euros.in
# puts 12.lats.in

# currencies = {'yen' => 0.013, 'euro' => 1.292, 'rupee' => 0.019, 'dollar' => 1.0, 'lat' => 2.0}
# puts currencies['yen']