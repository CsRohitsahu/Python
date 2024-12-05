
import os 
os.chdir('File handling')
f=open('demo.txt','r')
# data=f.read() # reads entire file
line1=f.readline().strip() # reads one line at a time and remove any whitesapce and \n
print(line1)

line2=f.readline()
print(line2)
f.close()

# with syntax automatically closes file
with open('demo.txt','r') as f:
 data=f.read();
    
 print(data)    




