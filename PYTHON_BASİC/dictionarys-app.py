## key - value pairs
users = { "Ela Sutdonduran" : {
            "age": 7,
            "city": "Istanbul",
            "is_student": True,
            "email": "ela@info.com",
            "phone_numbers": ["05551112233"]},

            "Kaan Sutdonduran" :
            {"age": 17,
            "city": "Istanbul",
            "is_student": True,
            "email": "kaan@info.com",
            "phone_numbers": ["05551114455"]}
}

print(("Ela's age : "),users["Ela Sutdonduran"]["age"])  # Accessing age of Ela
print(users["Kaan Sutdonduran"]["phone_numbers"][0])  # Accessing Kaan's first phone number
users["Ela Sutdonduran"]["age"] = 8  # Modifying Ela's age
print("Ela's updated age:", users["Ela Sutdonduran"]["age"])    
users["Kaan Sutdonduran"]["phone_numbers"].append("05551119999")  # Adding a new phone number for Kaan
print("Kaan's updated phone numbers:", users["Kaan Sutdonduran"]["phone_numbers"])
users["Ayse Yilmaz"] = {
    "age": 25,
    "city": "Ankara",
    "is_student": False,
    "email": "ayse@info.com"}  # Adding a new user
print(users)


new_students = {}

number = input("Number of students to add: ")
fullName = input("Student Fullname :  ")
age = input("Student Age :  ")
phone = input("Student Phone :  ")

new_students.update({
    number: {
    "Fullname": fullName,
        "age": age,
        "phone": phone
}})
number = input("Number of students to add: ")
fullName = input("Student Fullname :  ")
age = input("Student Age :  ")
phone = input("Student Phone :  ")

new_students.update({
    number: {
    "Fullname": fullName,
        "Age": age,
        "Phone": phone
    
}})

ogrNo = input("Student Number : ")
student = new_students[number]
print(student)