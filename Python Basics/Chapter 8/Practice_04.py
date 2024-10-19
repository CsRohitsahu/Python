
# write a recursive function to print sum of nth natural number
def sum(n):
 if n==0:
  return 0   
 return n+sum(n-1)
a=int(input("Enter value you want to find sum of :"))   
print("sum of natural no. you entered is :",sum(a))
