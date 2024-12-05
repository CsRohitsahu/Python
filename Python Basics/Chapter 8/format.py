'''string formating refers to process of inject or embeding values into string in a structured way'''

#method 1 ->  using format()
name ="Rohit"
age=22
dept="IT"
text="My Name is {}\nage is {}\ndepartment of {}".format(name,age,dept)
print(text)

# method 2-> using % operator
name = "Alice"
age = 30.9909
print("Hello, %s. You are %.2f years old." % (name, age))

#method 3-> using f string

name ="Rohit"
age=22
dept="IT"
print(f"My name is {name}\nage is {age}\ndepartment of {dept}")
