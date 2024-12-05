# write a programme to find greetest of three no. using function
def Maximum(num1,num2,num3):
    if(num1>num2):
        return num1
    else:
        return num2    
    if num1>num3:
        return num1
    else:
        return num3
print("Enter 3 no. you want to compare")                
a=int(input("Enter first no.:"))
b=int(input("Enter second no.:"))
c=int(input("Enter third no."))
print("maximum of 3 no. is :")
print(Maximum(a,b,c))