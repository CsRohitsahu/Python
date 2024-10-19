#Write a Python program to display a user-entered name followed by
# Good Afternoon using input() function.
'''name=input("Enter your name:\n")
print("Good Afternoon,"+name)'''

''' Write a program to fill in a letter template given below with name and date.
letter = ‘’’ Dear <|NAME|>,

                        You are selected!

                        <|DATE|>'''

# letter=''' Dear <|Name|>, 
# Greeting from Google . I am glad to tell you that your selected in our 
# company.
# You are selected!
# 
# Date:<|Date|>'''
# 
# name =input("Enter your name \n")
# date=input("Enter Date\n")
# letter=letter.replace("<|Name|>",name)
# letter=letter.replace("<|Date|>", date)
# print(letter)


# Write a program to detect double spaces in a string.
'''st="This is string with double   spaces"
doubleSpaces=st.find("  ")
print(doubleSpaces)
print(st)
print(st.replace("  ", ""))# replacing double spaces with single spaces'''

'''Write a program to format the following letter using escape sequence characters.
letter = “Dear Rohit, This Python course is nice. Thanks!!”'''
'''letter="Dear Rohit, This  Python course is nice. Thanks!!"
print(letter)
print("printing formetted letter below:")
formatted_letter="Dear Rohit, \n\tThis Python course is nice!\n Thanks"
print(formatted_letter)'''
