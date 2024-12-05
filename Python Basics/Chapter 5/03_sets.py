# set is unordered collection of data that is mutable


# a={1,4,5,3,5}
# # print(type(a))
# a.add(90)
# print(a)
b=set()
print(type(b))
# adding element in empty sets
b.add(1)
b.add(2)
b.add(3)
b.add(23)
b.add(21)
b.add(31)
b.add((4,3,2,2))
print("printing element of set b")
print(b)
# print(len(b))# prints the length of sets
# b.remove(2)# remove the element from sets
# print("printing the element after removing entered element")
# print(b)

print(b.pop())#Removes an arbitrary element from the set and returns the element removed

