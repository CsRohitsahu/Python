# write a programme to find greaest of four numbers entered by user
'''num1=int(input("Enter number 1:"))
num2=int(input("Enter number 2:"))
num3=int(input("Enter number 3:"))
num4=int(input("Enter number 4:"))
if(num1>num4):
    f1=num1
else:
    f1=num4
if num2>num3:
    f2=num2
else:
    f2=num3
if f1>f2:
    print(f1,"is greatest")
else:
    print(str(f2)+"is greatest") '''
   # ->>Write a program to find out whether a student is pass or fail if it requires a total of 40% and at least 33% in each subject to pass.
   #  Assume 3 subjects and take marks as an input from the user.
'''sub1=int(input("Enter mark of subject 1:"))
sub2=int(input("Enter mark of subject 2:"))
sub3=int(input("Enter mark of subject 3:"))
if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have achieved less than 33% in each subject")
elif(sub1+sub2+sub3)/40:
    print("You are fail because total percentage is less than 40%")    
else:
    print("congratulations, you are passed")'''

   # ->>A spam comment is defined as a text containing the following keywords:
# “make a lot of money”, “buy now”, “subscribe this”, “click this”.
#  Write a program to detect these spams     
'''text=input("Enter the text:")
spam=False
if("make a lot of money" in text):
    spam=True
elif("buy now" in text):
      spam=True
elif("subscribe this" in text):
    spam=True
elif("click this" in text):
    spam=True
else:
    spam=False
if(spam):
    print("This text is spam")
else:
    print("This text is not spam") '''       
# write a programme to find whether a given username contains less than 10 characters 
'''name=input("Enter user name:")
if(len(name)<10):
    print("character in name entered by user is less than 10")
else:
    print("character in name entered by user is greater than or equal to 10")   '''
      
   
  
