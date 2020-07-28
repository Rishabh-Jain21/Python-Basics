print("different format pattern")
print(format(13402.4525, '.2f'))
print(format('hello', '.<30'))
print(format('hello', '>30'))
print('hello', format('.', '.<30'), 'Have a nice day')
print(format('hello', '^30'))
print(format('', '-<10'), "Thank you", format('', '->10'))
x = 12
print(format(x, 'b'))
print(format(x, 'x'))  # x for hexa
print(format(x, 'o'))
print(format(2**32+x, 'b'))
print(format(2**32+x, 'x'))
