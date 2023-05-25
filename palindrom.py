num=int(input("enter a number"))
temp=num
rev=0
while(num>0):
    digt=num%10
    rev=rev*10+digt
    num=num//10
if(rev==temp):
    print("palindrome")
else:
    print("not a palindrome")



