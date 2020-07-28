values = list(range(5))
print(values)
values = [*range(5)]
print(values)
print(*values)

new = [*values, *"hello"]
print(new)
list1 = list(range(0, 6))
list2 = list(range(6, 10))
print(*list1, *list2)
print(*list1, "a", *list2, *'hello')


first = {'x': 1}
second = {'x': 10, "y": 2}
combined = {**first, **second}
print(combined)  # last value of second dictionary is priorityand it is used
