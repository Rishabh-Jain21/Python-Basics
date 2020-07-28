# Any
# Returns True if any element of an iterable is True and False otherwise
# At least one value is True --> True
# All values are False --> False
# Empty iterable --> False

fruits = ['apple', 'pineapple', 'watermelon', 'avocado']
fruits_mapped = map(lambda fruit: fruit.startswith('a'), fruits)
# print(list(fruits_mapped)) #mapped objects are destroyed if converted to list dict or anything
print(any(fruits_mapped))

fruits_mapped = map(lambda fruit: len(fruit) > 50, fruits)
print(any(fruits_mapped))
print(any([]))


# All
# Return True if all elements of an iterable is true and False otherwise
# At least one value is Flase --> False
# All values True --> True
# Empty iterable --> True

fruits_mapped = map(lambda fruit: fruit.startswith('a'), fruits)
print(all(fruits_mapped))

fruits_mapped = map(lambda fruit: len(fruit) < 50, fruits)
print(all(fruits_mapped))
