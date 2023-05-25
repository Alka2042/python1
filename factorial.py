num=int(input("enter the number"))
fact=1
for n in range(1,num+1):
    fact=fact*n
print(fact)



def fact(num):
    if num==0:
        return num
    else:
        return num*fact(num-1)

print("factorial:",fact(5))



