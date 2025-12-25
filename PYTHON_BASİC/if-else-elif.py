
name = input("Your name : ")
age = int(input("your age : "))
education = input("Your education level : ")

if age >= 18:
    if education == "university" or education == "high school":
        print(f"{name}, you are eligible to get a driver's license.")
    else:
        print(f"{name}, you must have at least a high school diploma to get a driver's license.")
else:
    print(f"{name}, you must be at least 18 years old to get a driver's license.")

print("--------------------------------------------------")

exam_one = float(input("First exam score : "))
exam_two = float(input("Second exam score : "))
oral_exam = float(input("Oral exam score : "))
average = (exam_one + exam_two + oral_exam) / 3

if average < 24:
    print("Your grade is 0")
elif 25 <= average <= 44:
    print("Your grade is 1")
elif 45 <= average <= 54:
    print("Your grade is 2")
elif 55 <= average <= 69:
    print("Your grade is 3")
elif 70 <= average <= 84:
    print("Your grade is 4")
elif 85 <= average <= 100:
    print("Your grade is 5")
else:
    print("incorrect information entered")

print("--------------------------------------------------")


import datetime
today = datetime.datetime.today()
date = int(input("Enter the vehicle's model year : "))
date = date.split("/")
traficDate = datetime.datetime(date[0]), (date[1]), (date[2])

if date == today.year:
    print("Your car is new. It's not time for maintenance yet.")
elif today.year - date == 1:
    print("Your car is 1 year old.Your vehicle's first service year.")
elif today.year - date == 2:
    print("Your car is 2 years old.Your vehicle's second service year.")
elif today.year - date == 3:
    print("Your car is 3 years old.Your vehicle's third service year.")
else:
    print("Your car is older than 3 years.You need to re-insure your vehicle.")

print("--------------------------------------------------")


    