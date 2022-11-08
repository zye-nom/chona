test = int(input("i scored"))
exams = int(input("i scored"))
total = test + exams
print(total)
if total < 50 or exams < 25:
    print("fail")
elif total >= 80:
    print("distinction")
elif 50 >= total <= 59:
    print("pass")
elif 80 >= total >= 60:
    print("credit")
elif 0 <= test >= 25 or 0 <= exams >= 50:
    print("error")

