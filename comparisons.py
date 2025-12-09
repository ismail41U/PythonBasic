
a = int(input("Enter a number : "))
b = int(input("Enter b number : "))
result = a > b
print(f"a > b : {result}")

user_midterm_one = int(input("Enter midterm_onescore : "))
user_midterm_two = int(input("Enter midterm_two score : "))
user_midterm = (user_midterm_one + user_midterm_two) * 0.6
user_final = int(input("Enter final score : "))
userFinal = user_final * 0.4
total_score = (user_midterm + userFinal) / 2
print("Total Score :", total_score)
if total_score >= 50:
    print(f"Student passed : {total_score}")
else:
    print(f"Student failed : {total_score}")

x = int(input("Enter x number : "))
if x % 2 == 0:
    print(f"{x} is even number")
else:
    print(f"{x} is odd number")

y = int(input("Enter y number : "))
if y >= 0:
    print(f"{y} is positive number")
else:
    print(f"{y} is negative number")
user = "Al Pacino"
code = "1649"
user_name = input("Enter your name : ")
if user_name == user:
    user_code = input("Enter your code : ")
    if user_code == code:
        print("Welcome Al Pacino")
    else:
        print("Wrong code")
else:
    print("Unknown user")