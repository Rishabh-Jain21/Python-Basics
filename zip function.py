from itertools import zip_longest
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 144, 446]
b = [10, 11, 12, 13, 14, 15, 16, 17, 18]
c = [44, 78, 41, 23, 56, 47, 86, 78, 45]
for x, y, z in zip(a, b, c):
    print(str(x)+' '+str(y)+" "+str(z))

# Zip considers shortest list
products = {'apple': .5, 'pineapple': .7}
tech_products = {'iphone': 1000, 'windows': 600}

products_tech = zip(products, tech_products)
print(list(products_tech))

products_tech = zip(products.values(), tech_products.values())
print(list(products_tech))

country = "India"
capital = "Delhi"
country_capital = zip(country, capital)
print(list(country_capital))

# for zip to consider longest list we use zip_longest
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 144]
b = [10, 11, 12, 13, 14, 15, 16, 17, 18]
c = [44, 78, 41, 23, 56, 47, 86, 78, 45, 16, 44]
for x, y, z in zip_longest(a, b, c):
    print(str(x)+' '+str(y)+" "+str(z))


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 144, 446]
b = [10, 11, 12, 13, 14, 15, 16, 17, 18]
c = [44, 78, 41, 23, 56, 47, 86, 78, 45]
for x, y, z in zip_longest(a, b, c, fillvalue="Not_Available"):
    print(str(x)+' '+str(y)+" "+str(z))
