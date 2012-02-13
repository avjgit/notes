=begin
# Chapter One 
print 'enter your name: '
name = gets
puts ('hello there, ' + name).upcase
### Strings and Embedded Evaluation 
puts "hello again #{name}"
def showname
  'fred'
end
puts "hello again #{showname}"
puts "\n\t#{(1+2)*3}"
### Methods 
def return_name (first, last)
  puts "hi #{first} #{last}"
end
def return_name2 first, last
  puts "hi #{first} #{last}"
end
return_name('a', 'j')
return_name2 'b', 'c'
# return_name2 ('b', 'c') - doesn't work!
### Numbers
subtotal = 100.0
### Testing a Condition: if < then 
taxrate = 0.175
print "enter another price: "
subtotal = gets.to_f
if (subtotal < 0.0) 
  subtotal = 0
end
tax = subtotal * taxrate
puts "and tax on #{subtotal} is #{tax}, so all together is #{subtotal+tax}"
=end
# Chapter Two 
### Instances and Instance Variables 
### Constructors – new and initialize 
### Inspecting Objects 
# Chapter Three
### Superclasses and Subclasses 
# Chapter Four 
### Accessor Methods 
### Attribute Readers and Writers 
### Attributes Create Variables 
### Calling Methods of a Superclass 
### Class Variables 
# Chapter Five 
### Using Arrays 
### Creating Arrays 
### Multi-Dimensional Arrays 
### Iterating Over Arrays 
### Indexing Into Arrays 
# Chapter Six 
### Creating Hashes 
### Indexing Into A Hash 
### Hash Operations 
# Chapter Seven 
### For Loops 
### Blocks 
### While Loops 
### While Modifiers 
### Until Loops 
# Chapter Eight 
### If, Then, Else 
### And, Or, Not 
### If, Elsif 
### Unless 
### If and Unless Modifiers
### Case Statements 
# Chapter Nine 
### A Module Is Like A Class 
### Module Methods 
### Modules as Namespaces 
### Module ‘Instance Methods’ 
### Included Modules or ‘Mixins’ 
### Including Modules From Files 
### Pre-Defined Modules 
# Chapter Ten 
### IronRuby and JRuby 
### Saving Data 
### YAML 
### Files 
### Moving On
