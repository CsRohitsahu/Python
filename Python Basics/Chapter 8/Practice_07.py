# write a python function to remove a given word from a string and
#  strip it at the same time
def remove_and_sptrip(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()
this="Rohit is student of University of Allahabad   "
n=remove_and_sptrip(this,"Rohit")    
print(n)
print(this.strip())