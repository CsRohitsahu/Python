f=open('demo.txt','w') # if there is not file exiting first it creates file with specified name then writes data inside
f.write("Hi everone\nwe are learning File I/O\nUsing Java\nI like programming in Java")
f.close()

# replacing all occurances of 'java' with 'python' in above file


with open('demo.txt','r') as f:
 data=f.read()

new_data=data.replace('Java','Python')   
print(new_data)

# one important things to note in above code data and new_data variable inside with block is not limited to only with block only f object is limited to with block




with open('demo.txt','w') as f:  
    f.write(new_data)  


    # search whether "learning exits in file or not"
word = 'learning'
with open("demo.txt", 'r') as f:
    data = f.read()
if data.find(word) != -1:
        print("found")
else:
        print("not found")






