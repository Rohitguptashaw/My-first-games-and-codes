
def abc(str1,str2):
    cont=0
    for i in range(len(str1)):
        if(str1[i:i+len(str2)]==str2):
            cont+=1
    return cont

str1=input("string1")
str2=input("sub")
q=abc(str1,str2)
print(q)

