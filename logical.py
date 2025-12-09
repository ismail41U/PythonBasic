
number = int(input("Enter a number: "))
print(f"Is the number between 0 and 100 ? : {number > 0 and number <= 100}")

print("--------------------------------------------------")

num = int(input("Enter a number: "))
print(f"Is the number even and pozitive ? {num %2 == 0 and num %2 >= 0}")

print("--------------------------------------------------")

e_mail = "ela@info.com"
code = 1234
email = input("Enter your email : ")
password = int(input("Enter your password : "))
print(f"Is email and password correct ? : {email == e_mail and password == code}")