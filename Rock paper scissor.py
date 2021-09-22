import random

def fun(comp,yc):
    if comp==yc:
        return None
    elif comp=='r' and yc=='s' or comp=='p' and yc=='r' or comp=='s' and yc=='p':
        return True
    else:
        return False
        
ran=random.randint(1,3)
if ran==1:
    comp='r'
elif ran==2:
    comp='p'
elif ran==3:
    comp='s'
        
yc=input("your choice in r p s")
    
        
        
print("Comp=" +comp)
print("you=" +yc)

q=fun(comp,yc)
if q==None:
    print("tie")
elif q==True:
    print("comp win")
else:
    print("you win")