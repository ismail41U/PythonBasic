
number = int(input("Enter a number: "))
print(f"Is the number between 0 and 100 ? : {number > 0 and number <= 100}")

print("--------------------------------------------------")

num = int(input("Enter a number: "))
print(f"Is the number even and pozitive ? : {num %2 == 0 and num %2 >= 0}")

print("--------------------------------------------------")

e_mail = "ela@info.com"
code = 1234
email = input("Enter your email : ")
password = int(input("Enter your password : "))
print(f"Is email and password correct ? : {email == e_mail and password == code}")

print("--------------------------------------------------")

studentMidterm1 = float(input("Enter student midterm score : "))
studentMidterm2 = float(input("Enter student midterm score : "))
studentMidterm = float(studentMidterm1 + studentMidterm2) * 0.6
studentFinal = float(input("Enter student final score : ")) * 0.4
totalScore = int(studentMidterm + studentFinal) / 2
print(f"Student total score : {totalScore}")
print((totalScore >= 50 and studentFinal >= 50) or totalScore >= 70)

print("--------------------------------------------------")

name = input("Enter your name : ")
size = float(input("Enter your size : "))
kilo = float(input("Enter your kilo : "))

endeks = ((kilo / size) ** 2)
print(f"Your weight index : {endeks}")
print(f"Is your weight weak: {endeks >= 0 and endeks <= 18.4}")
print(f"Is your weight under normal : {endeks >= 18.5 and endeks <= 24.9}")
print(f"Is your weight overweight  : {endeks >= 25 and endeks <= 29.9}")
print(f"Is your weight obese  : {endeks >= 30 and endeks <= 34.9}")

print("--------------------------------------------------")