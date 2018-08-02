# x=5
# y=10

# while x!=11 :

#     if x<y :
#         print("limit not exceeded")
#         x = x + 1

#     else :
#         print("limit exceeded")
#         break


# fruits = ["apple", "banana", "cherry"]
# for item_fruit in range(3):
#   print(fruits[item_fruit])


# x = lambda a, b : a + 10 + b
# print(x(5,1))

# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))

# cars = ["Ford", "Volvo", "BMW"]
# print(cars[2])
# cars.append("suzuki")
# print(cars[3])

import mymodule
import platform
import datetime
import json
import os

mymodule.greeting("ZAID")


class MyClass:
    x = 5


p1 = MyClass()
# print(p1.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


x = datetime.datetime.now()

print(x.year)
print(x.strftime("%a"))


# # some JSON:
# x =  '{ "name":"zaid", "age":22, "city":"Lahore"}'

# # parse x:
# y = json.loads(x)

# # the result is a Python dictionary:
# print(y["name"])


# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# # convert into JSON:
# y = json.dumps(x)

# # the result is a JSON string:
# print(y)

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print( json.dumps(x, indent=2, sort_keys=True))


f = open("demofile.txt")

f = open("demofile.txt", "rt")
f = open("demofile.txt", "r")
print(f.read())

f = open("demofile.txt", "a")
f.write("Now the file has one more line!")

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
else:
    print("The file does not exist")
