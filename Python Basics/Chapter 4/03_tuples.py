# Creating tuple , tuple is immutable means it item cann't be updated or added
t=(1,2,4,5)
# t1=()# Empty tuple
# t1= (1) # wrong way to define tuple with single element treated as int datatype 
# t1=(1,)# tuple with single element 
# print(t1)
# Printing element of tuple
# print(t[0])
 # Cannot update the values of a tuple 
#  t[0]=32--> throws an ()

print("finding no. of occurance of a element  in tuples ")
print(t.count(1))
print("methods to return index of first occurance of a tuple ")
print(t.index(5))  # 5 is here value not index

