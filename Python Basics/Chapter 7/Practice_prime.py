# --> write a programme to find whether a entered no is prime or not
n=int(input ("Enter no. you want to check:"))
prime=True
for i in range(2,n):
    if n%i==0:
        prime=False
        break
if prime:
    print("This is Prime number")    
else:
    print("This is not prime no.")    


n=int(input("enter no"))
for i in range(2,n):
    if n%i==0:
        print(f"{n} is not prime")
        break;
    else :
        print(f"{n } is prime") 
        break;   
