def lo():
    e=99
    print(e)# here treated local e=99
e=8
lo()
print(e)#here treated global



def glo():
    global a # changed globally not locally
    a=6 

a=4
glo()
print(a)
