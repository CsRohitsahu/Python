from math import factorial


n=int(input("Enter no. you want find factorial of :"))
factorial=1
for i in range(1,n+1):
    factorial*=i
print("factorial of entered no. is :")
print(factorial)