f=open('demo.txt','r+')
f.write('college')  # it overides content of file not truncating whole content
f.seek(0) # this methods set file pointer to beginning 
print(f.read())
f.close()