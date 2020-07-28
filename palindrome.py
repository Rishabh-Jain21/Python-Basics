print("program for palindrome")

s=0
num=int(input("enter number"))
n=num
while n>0:
    rem=n%10
    s=10*s+rem
    n=n//10

if num==s:
    print("given is palindrome")
else:
    print("not palindrome")

    

