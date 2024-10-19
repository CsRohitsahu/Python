f=open('demo.txt','w+')

f.write(" created new file") # first file is truncated
f.seek(0)
data=f.read()
print(data)

f.close()