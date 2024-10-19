'''Write a program to print the following star pattern:
*

**

*** for n = 3'''
'''n=4
for i in range(4):
  print("*"*(i))
  Write a program to print the following star pattern.
    *

  ***  

***** for n=3'''
n=3
for i in range(3):
  print(" "*(n-i-1),end="")
  print("*"*(2*i+1),end="")
  print(" "*(n-i-1))
