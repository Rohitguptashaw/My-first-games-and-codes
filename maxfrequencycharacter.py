a=input("string")
b={}
l=len(a)
for i in a:
    if i not in b:
        b[i]=a.count(i)
print(b)
# z=max(b)
# print(z)
t=max(b.items(),key = lambda b:b[1])
print(t)


