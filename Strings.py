a="helloworld"
print(a)
print(a[0])
print(a[0:5])

print(a.isupper())
print(a.islower())
print(a.isalpha())#letters only
print(a.isdecimal())#numbers only
print(a.isalnum())#numbers and letters only
print(a.isspace())#whitespaces only
print(a.istitle())# titlecase only

print(a.ljust(20))# left justify add spaces to left
print(a.rjust(20))# right justify add spaces to right

print(a.ljust(20,'-'))
print(a.rjust(20,'*'))
print(a.center(20))
print(a.center(20,'*'))

b='india'
c='china'
d='america'

country=b+' '+c+' '+d+' are countries'
print(country)
con='%s %s %s are countries' %(b,c,d)
print(con)
