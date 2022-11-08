# tuples
attendants = ("alicent", "alex", "meg", "dave", "sierra", "meg")
print(attendants)

print(attendants[2])

print(attendants)
print(len(attendants))

print(attendants[-4])

if "matt" in attendants:
    print("name present")
else:
    print("absent")

if "alex" in attendants:
    print("present")
else:
    print("absent")

presentees = list(attendants)
print(presentees)
presentees[-3] = "phil"
print(presentees)
attendants = tuple(presentees)
print(attendants)

names = ("eanu", "jess", "emma", "josh")
(first, second, *other_people) = names
print(first)
print(second)
print(other_people)
# if the number of variables is less than the number of values
# you can add * to the variable as a list

for people in names:
    print(people)

names_of_attendants = attendants + names
print(names_of_attendants)
quantity = names * 8
print(quantity)

numbers = (1, 2, 4)
for number in numbers:
    print(number + 5)

menu = ("rice", "beans", "yam", "potato")
print(menu)
for item in menu:
    print(item)
new_menu = list(menu)
print(new_menu)
new_menu[2] = "samosa"
print(new_menu)
new_menu[0] = "bread"
print(new_menu)
main_dish = tuple(new_menu)
print(main_dish)
for food in main_dish:
    print(food)

digits = (4, 5, 6, 7)
max_number = 0
for digit in digits:
    if digit > 0:
        max_number = digit
print(max_number)

# sets used to store multiple items in a single
# variable
# unordered
# unchangeable
# do not allow duplicates
# unindexed
# to add two sets use .update functions
# to add item in set use .add function
# to remove item use .remove function
# to remove last item use pop

intro = {"jess", "21", "kaduna", "afit"}
print(intro)
for myself in intro:
    print(myself)
print("jess" in intro)

intro.add("virgo")
print(intro)

# adding two sets and removing an item from a set
hobbies = {"watching movies", "writing", "texting", "singing"}
print(hobbies)
intro.union(hobbies)
hobbies.remove("watching movies")
print(hobbies)
her = intro.pop()
print(her)
print(intro)

# clearing a set
sister = {"commy", "28", "march", "tall"}
print(sister)
sister.clear()
print(sister)

# loop
for writing in intro:
    print(writing)

# intersection
jess = {"cat", "dog", "pets"}
nora = {"animals", "dogs", "cat"}
jess.intersection_update(nora)
print(jess)
# behaves like the intersection in maths


land_animals = {"cows", "lions", "tigers", "horses", "cheetah"}
herbivores = {"cows", "goats", "horses", "deers", "rams"}
land_animals.symmetric_difference_update(herbivores)
print(land_animals)
# the symmetric_difference_update will keep only the element
# that are not present in both sets


x = {"apple", "pear", "orange", "banana"}
y = {"mango", "pineapple", "orange", "grapes", "cucumber"}
veg = x.symmetric_difference(y)
print(veg)

# dictionaries
# curly braces like set
# changeable, ordered
# store data in key_value terms
musa_family = {"first": "nasiru", "second": "noel", "third": "nora"}
print(musa_family)

ages = {"first": 33,
        "second": 31,
        "third": 29,
        "fourth": 26,
        "fifth": 20

        }
print(ages)
ages["first"] = "37"
print(ages)

# to determine length
print(len(ages))

identity = {"me": "jess",
            "age": "21",
            "christian": "true",
            "school": ["stat", "300l", "afit"]
            }
print(identity)

details = identity["school"]
print(details)

# get values
mood = identity.values()
print(mood)
# get keys
made = identity.keys()
print(made)

if "religion" in identity:
    print("yes")
else:
    print("not available")

identity["address"] = "kaduna"
print(identity)
identity.pop("address")
print(identity)

for id in identity:
    print(id)

for x, y in identity.items():
    print(x, y)

# nested dictionaries
musaFAMILY = {
    "firstson": {
        "name": "isaac",
        "year": 1987
    },
    "secondson": {
        "Name": "noel",
        "Year": 1989
    },
    "firstdaughter": {
        "nAme": "nora",
        "yEar": 1991
    }
}

print(musaFAMILY)

if "secondson" in musaFAMILY:
    print("yes")
else:
    print("mistake")

for head in musaFAMILY:
    print(head)

nasiru = musaFAMILY.keys()
print(nasiru)

# functions or method
firstnumber = 10
secondnumber = 20
print(firstnumber + secondnumber)


# def james():
#   firstnumber = 10
#   secondnumber = 20
#    print(firstnumber + secondnumber)


# james()

# james()



# a function is a group of code that performs a particular task
# to define your function, you use the def keyword followed by the name
# of the function to be followed by parentheses, them everything that has
# to be in the function has to be indented

# example
def saymyname():
    return "daddy"

print(saymyname())

# functtions also accept parameters or arguments
# name in parenthsesis is called a parameter,
# to call the function you need to pass a value

def f_1():
    print('hello world')

f_1()


# task
def sumsubmul(firstn, secondn):
    print(firstn + secondn)
    print(firstn - secondn)
    print(firstn * secondn)

sumsubmul(40, 30)

# arbitrary arguments
def displaymyname(*names):
    for name in names:
        print(names[2])


displaymyname("jess", "nas", "musa", "nora")
# to access  SPECIFIC ITEM USE THE TUPLE

# lambda functions are anonymous functions
def sumofnumbers(jess, chona):
    print(jess + chona)

rela = lambda jessy, gabe : jessy + gabe
print(rela(20, 10))


l = lambda x : x + 2
print(l(9))

f = lambda a, b: a * b
print(f(9, 6))

x = lambda name: "hello" + " " + name
print(x("nifemi"))

# python while loops
x = 1
while x < 6:
    print(x)
    x += 1
print("end of loop")

x = 1
while x < 6:
    x = x + 1
print("end of loop!!!!")

# break statement
#we can stop the loop even if the condition is true
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i = i + 1



# the continue statement
# we can stop the current iteration and continue with
# the next
i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)

#else statement
# we can run a block of code once when the condition is
# not true

j = 1
while j > 6:
    print(j)
    j +=4
else:
    print("j is greater than 6")

# exercise
for i in range(1,51):
     print(i)

x = 1
while x < 51:
    print(x)
    x = x + 1

#getusername = input("what is your name")
#while getusername != "smallie":
#    getusername = input("try again")
#else:
#    print("welcome smallie")

#number = int(input("enter a number"))
#while number != 999:
#    number = int(input("input another"))
#else:
#    print("end of program")


# figure = int(input("enter"))
# while figure != 999:
#    if figure % 2 == 0:
#        print("good job")
#        figure = int(input("enter another"))
#    else:
#        print("error")
#        figure = int(input("enter another"))
# else:
#    print("the end ")

#word = input("enter a word")
#while word != " ":
#    word = input("again")
#else:
#    print("end")

PYTHON MODULE IS A COLLECTION OF FUNCTIONS 



