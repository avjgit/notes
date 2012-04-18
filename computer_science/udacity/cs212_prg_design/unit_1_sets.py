# set: an unordered collection of elements with no duplicates

fruit = set(['apple', 'orange', 'tomato'])
vegetable = set(['brocolli', 'tomato', 'carrot'])

print(fruit)
print(fruit - vegetable)
# print(fruit + vegetable) # doesn't work
print(fruit | vegetable)
print(fruit & vegetable)
print(fruit ^ vegetable)