v="your creativity is at its best while insulting one another"

s=v.split()

l=["a","e","i","o","u"]
for word in s:
    if word[0].lower() in l:
        print(word)
#tuple

t=(12,34,5.6,90)

#dict

d={"Language":"python","rating":7,9:4}
print(d["rating"])
print(d.get("rat"))
printd.update({"founder":"guide van rossum"})
print(d)
print(d.items())
print(d.keys())
print(d.values())
print(d.pop("rating"))
print(d)
print(d.popitem())


students={"Name":["Alka","akshay"],'age':[25,24]}

print(students)