import pprint
a=(input())
count={}
for i in a.lower():
    count.setdefault(i,0)
    count[i]=count[i]+1

pprint.pprint(count)
    
