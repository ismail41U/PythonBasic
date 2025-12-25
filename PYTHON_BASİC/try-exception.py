
myList = ["1", "2", "10a", "40b", "50c", "60", "70d"]
myDigit = []
for item in myList:
    try:
        num = int(item)
        myDigit.append(num)
    except ValueError:
        continue

print("Final list of integers:", myDigit)

print("------------------------------------------------")

while True:
    userInput = input("Enter a number : ")
    if userInput == 'q':
        print("Exiting the program.")
        break
    try:
        number = int(userInput)
        print(f"You entered the number: {number}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

print("------------------------------------------------")

password = "secure123"
attempts = 3

while attempts > 0:
    userInput = input("Enter your password: ")
    try:
        chars = "çğıöşüÇĞİÖŞÜ"
        if any(char in chars for char in userInput):
            raise ValueError("The password cannot contain Turkish characters !")
        
        if userInput != password:
            raise ValueError("Incorrect password!")
        print("Access granted.")
        break
    except ValueError as ve:
        attempts -= 1
        print(ve)
        if attempts == 0:
            print("No attempts left. Access denied.")
        else:
            print(f"You have {attempts} attempts left.")