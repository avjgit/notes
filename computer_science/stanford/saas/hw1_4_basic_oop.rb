# Part 4: Basic OOP
# (a) Create a class Dessert with getters and setters for name and calories.  Define 
# instance methods healthy?, which returns true if a dessert has less than 200 
# calories, and delicious?, which returns true for all desserts.
# (b) Create a class JellyBean that extends Dessert, and add a getter and setter for 
# flavor.  Modify delicious? to return false if the flavor is black licorice (but delicious? 
# should still return true for all other flavors and for all non-JellyBean desserts).Here is the framework (you may define additional helper methods):

class Dessert
    def initialize(name, calories)
    # YOUR CODE HERE
    end
    def healthy?
    # YOUR CODE HERE
    end
    def delicious?
    # YOUR CODE HERE
    end
    end
    class JellyBean < Dessert
    def initialize(name, calories, flavor)
    # YOUR CODE HERE
    end
    def delicious?
    # YOUR CODE HERE
    end
end