thislist="apple","Banana","cherry"
print(thislist)

new=['a','b','c']
print(new)

# thislist[0]="Mango"
# print(thislist)      it will show an error

new[0]='e'  # Changes item of given index 
print(new)


print("Using list command")
#  mylist=list("I","Me","Myself")  error is displayed
# print(mylist)   
mylist=list(("I","Me","Myself"))
print(mylist)

mylist.append("You")
print(mylist)
print(mylist[3])

mylist.remove("You")
print(mylist)
mylist.append("You")
print (mylist)

print(len(mylist))
print(mylist.count("You")) # count number of "you"

print(mylist.sort())



