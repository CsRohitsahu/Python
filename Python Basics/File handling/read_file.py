f=open('demo.txt','r')
# data=f.read() # reads entire file
line1=f.readline() # reads one line at a time
# print(line1)
line2=f.readline()
print(line2)
f.close()

# with syntax automatically closes file
'''with open('demo.txt','r') as f:
    data=f.read();
    
    print(data)    '''