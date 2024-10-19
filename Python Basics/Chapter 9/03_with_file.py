with open('rohit.txt', 'r') as f:
    a=f.read()
    print(a)
with open('rohit.txt','w') as f:
    a=f.write("me too")
print(a)        