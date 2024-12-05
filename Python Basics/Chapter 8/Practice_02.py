# Write a python program using the function to convert Celsius to Fahrenheit.
def convert(cell):
    F = cell*(9/5)+32
    return F
a=float(input("enter celsius:"))  
print("celsius to farenhet conversion is:",convert(a))
