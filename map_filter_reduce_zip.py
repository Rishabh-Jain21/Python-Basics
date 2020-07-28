from functools import reduce

my_list = [1, 2, 3]
your_list = [10, 20, 30]


def multiply_by2(item):
    return item*2


def only_odd(item):
    return item % 2 != 0


def accumulator(acc, item):
    print(acc, item)
    return acc+item


print(list(filter(only_odd, my_list)))
print(my_list)
print(list(map(multiply_by2, my_list)))
print(list(zip(my_list, your_list)))
print((reduce(accumulator, my_list, 0)))

fruits = ['apple', 'mango', 'orange', 'avocado']
filtered_fruits = filter(lambda fruit: fruit.startswith('a') == True, fruits)
print(list(filtered_fruits))


fruits = {'apple': 70, 'mango': 40, 'orange': 15, 'avocado': 200}
filtered_fruits = filter(lambda t: t[1] > 40, fruits.items())

print(dict(filtered_fruits))
print(list(filtered_fruits))
