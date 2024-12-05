# n!=1*2*3*...*n




'''def factorial_iter(n):
    product=1
    for i in range(n):
     product=product*(i+1)
    return product
a=int(input("Enter no. you want to find factorial of:"))
print(factorial_iter(a))'''


def factorial_recursion(n):
    if n==1 :
        return 1
    return n*factorial_recursion(n-1)   
a=int(input("Enter no. you want to find factorial of:"))     
f=factorial_recursion(a)
print(f)


