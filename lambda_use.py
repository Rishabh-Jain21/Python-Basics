from functools import reduce
from itertools import accumulate
from operator import mul
my_list = [1, 2, 3]
your_list = [10, 20, 30]


print(list(filter(lambda item: item % 2 != 0, my_list)))
print(my_list)
print(list(map(lambda item: item*2, my_list)))
print(list(zip(my_list, your_list)))
print((reduce(lambda acc, item: acc+item, my_list, 0)))


new_list = [1, 2, 3]
print(list(map(lambda k: k**2, new_list)))

a = [(0, 2), (4, 3), (9, 9), (10, -1)]
print(a.sort(key=lambda k: k[1]))
print(a)

lambda_list = [lambda x:x+j for j in range(3)]
for func in lambda_list:
    print(func(2))  # Output for all is 4 but in thory it should be 2 3 and 4.Lambda execute at runtime so it took last value of j that is 2 so lambda becoms x:x+2 fo all


print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
'''
1+2
(1+2)+3
((1+2)+3)+4
(((1+2)+3)+4)+5
'''
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5],
             15))  # sum=25 starts with 15 and is added
print("**********************")
numbers = [1, 4, 7, 3, 2]
result = (accumulate(numbers, mul))
print(list(result))

print("**********************")
for step in result:
    print(step)
