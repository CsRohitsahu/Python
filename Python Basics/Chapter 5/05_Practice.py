# Write a program to create a dictionary of Hindi words with
#  values as their English translation. Provide the user with an option to look it up!
'''myDict={
    'Janwar':'Animal',
    'Vastu':'Things',
    'Chasma':'Glasses',
    'Kapda':'Clothes'
}
print("Available option are:")
print(myDict.keys())
a=input("Enter word from available option:")
print("meaning of entered word is:")
# print(myDict[a])
#Below line will not fetch a error when entered word is not in dictionary
print(myDict.get(a))'''
#Write a program to input eight numbers from the user and display all the 
# unique numbers (once).


'''n3=int(input("Enter number 3:"))
n2=int(input("Enter number 2:"))
n4=int(input("Enter number 4:"))
n1=int(input("Enter number 1:"))
n5=int(input("Enter number 5:"))
n6=int(input("Enter number 6:"))
n7=int(input("Enter number 7:"))
n8=int(input("Enter number 8:"))
set={n1,n2,n3,n4,n5,n6,n7,n8}

print("printing value of set", set)'''
# What will be the length of the following set S:
'''S = set()
S.add(20)
S.add(20.0)
S.add("20")
print(len(S))'''
# Create an empty dictionary. Allow 4 friends to enter their favorite language as
#  values and use keys as their names. Assume that the names are unique.
favlang={}
a=input("Enter your favourite language Rohit:")
b=input("Enter your favourite language Mohit:")
c=input("Enter your favourite languagae Amit:")
d=input("Enter your favourite languagae Radh:")
favlang['Rohit']=a
favlang['Mohit']=b
favlang['Amit']=c
favlang['Radha']=d
print(favlang)

