# Part 4: Basic OOP
# (a) Create a class Dessert with getters and setters for name and calories.  Define 
# instance methods healthy?, which returns true if a dessert has less than 200 
# calories, and delicious?, which returns true for all desserts.
# (b) Create a class JellyBean that extends Dessert, and add a getter and setter for 
# flavor.  Modify delicious? to return false if the flavor is black licorice (but delicious? 
# should still return true for all other flavors and for all non-JellyBean desserts).Here is the framework (you may define additional helper methods):

class Dessert
    attr :name, true
    attr :calories, true
    def initialize(name, calories)
        @name = name
        @calories = calories    
    end
    def healthy?
        return @calories < 200 ? true : false 
    end
    def delicious?
        true
    end
end
class JellyBean < Dessert
    attr :flavor
    def initialize(name, calories, flavor)
        super(name, calories)
        @flavor = flavor
    end
    def delicious?
        if @flavor == 'black licorice'
            return false
        end
        super
    end
end

# tests
# d1 = Dessert.new('d1', 100)
# d2 = Dessert.new('d2', 200)
# puts d1.delicious?
# puts d2.delicious?
# puts d1.healthy?
# puts d2.healthy?

j1 = JellyBean.new('j1', 100, 'vanilla')
j2 = JellyBean.new('j2', 200, 'black licorice')
puts j1.healthy?
puts j2.healthy?
puts j1.delicious?
puts j2.delicious?