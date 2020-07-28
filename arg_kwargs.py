def super_func(*args, **kwargs):
    print(args)
    print(*args)

    print(type(args))

    print(type(kwargs))
    print(kwargs)
    print(*kwargs)
    total = 0
    for items in kwargs.values():
        total += items

    return sum(args)+total


print(super_func(1, 2, 3, 4, 5, num1=5, num2=10))

# RULE : param,*args,default parameters,**kwargs
