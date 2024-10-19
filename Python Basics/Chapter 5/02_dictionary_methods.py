myDict={
    'Fast': 'I am a boy',
    "Rohit":"A student",
    "Marks":"[2,3,4]",

    "anotherdict":{
        'rohit': 'player',
        'mohit': 'looser',
      
    },
      1:2,
      "age":22

    }

  
# print(myDict.keys())  # prints all keys of dictionary
# print(type(myDict.keys()))
# print(list(myDict.keys()))# prints the list of  key of the dictionary
# print(list(myDict.values()))# prints the list of  value of the dictionary
# print(myDict.items())# prints the (key, value ) for all the content in the dictionary
# print(myDict)
updateDict1={
    "Lovish": "Friend"
}
myDict.update(updateDict1)# update the dict by adding key values pairs from updateDict
# print(myDict)
# print(myDict.get("Rohit"))# prints  value associated with Rohit
# myDict.clear()  #delete all key , value of dictionary


# print(myDict.pop('Rohit')) # pops element with specified key and returns value associated with key
# print(myDict.popitem())  # removes last inserted items and returns that value 
# del myDict['Marks']  # deltes the item of dictionary with specified key name 

