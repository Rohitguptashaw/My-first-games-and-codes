arr = []
n = int(input("enter size of array : "))
for x in range(n):
    x=int(input("enter element of array : "))
    arr.append(x)
largest = arr[0]
smallest = arr[0]
for i in range(n):
    if arr[i]>largest:
        t=largest
        largest = arr[i]
    if arr[i]<smallest:
        smallest = arr[i]
        
print(f"largest element in array is {largest}")
print(f"smallest element in array is {smallest}") 
print(t)