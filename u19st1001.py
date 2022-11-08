animal = ("cat")
name = ("kelly")

#appwnd function
pets = ["cats", "birds", "dogs", "rabbits", "peacocks", "deer"]
pets.append("cow")
print(pets)

#loop through a list
for pet in pets:
    print(pet)
    print("hello")


#loop through a list and append
names = ["jess", "sammy", "leo", "matt"]
newlist = []
for x in names:
    newlist.append(x)
print(newlist)

#change a range of values in lists
names[2:4] = ["nora", "mews", "noel"]
print(names)

#exercise
numbers = [2, 3, 4, 5, 6, 7, 8, 9]
for element in numbers:
    if element % 2 == 0:
        print(element)



digits: list[int] = [3, 4, 5, 6, 7, 8, 9]
for digit in digits:
    if digit % 2 == 1:
        print(digit)

#remove specified item
digits.remove(4)
print(digits)

#remove specified index
digits.pop(3)
print(digits)

#

#'while loop
x = 1
while x < 6:
    print(x)
    x += 1
    print("end of loop")

for i in range(1,51):
    print(i)

while x < 51:
    print(x)
    x = x + 1

username = input("what is your name")
list_of_usernames = ["emma", "batul", "amir", "hassan"]
while username in list_of_usernames:
    username = input("username available")
else:
    print("click the box below to sign in")





