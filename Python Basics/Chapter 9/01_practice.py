# write a programme to  read the text from a given file, “poems.txt” and find out whether
#  it contains the word ‘Twinkle’.
   # creating poems.txt file
with open('poems.txt','w') as f:
    a=f.write('''Twinkle Twinkle little star 
    How I wonder what you are!''')
    # Reading poems.txt file
f=open("poems.txt")    
t=f.read()
if 'Twinkle' in t:
    print("Twinkle is present")
else :
    print("Twinkle is not present")  
f.close()      