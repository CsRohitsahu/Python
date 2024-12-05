# use open function to read the content of file
#f=open("rohit.txt", 'r')
f=open('rohit.txt','r')# by default the mode is r
# data=f.read()
# data=f.read(4)# Read first four characters of the file
data=f.readline()# Reading line of file
print(data)
f.close()