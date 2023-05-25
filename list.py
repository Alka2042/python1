numbers=[n for n in range(1,52) if n%2==0]
print(numbers)

num=int(input("enter the number"))
for n in range(1,11):
    print(f"{n}*{num}={n*num}")

num=int(input("enter the number"))
for i in range(0,num):
    for j in range(0,i+1):
        print("*")

for r in range(1, 6):
    print("*" * r)
