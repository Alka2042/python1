number=int(input("ente number"))
temp=number
digt=0
while(number>0):
    n=number%10
    digt+=n**len(str(temp))
    number=number//10
if(temp==digt):
    print("amstrong")
else:
    print("not amstrong")
