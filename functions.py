def changeName(n):
    n = "Ela"
    
name = "Kaan"

changeName(name)
print(name)  # This will print "Kaan" because strings are immutable and,
             # he change inside the function does not affect the original variable.

print("------------------------------------------------------------------------------")

def changeCity(city):
    city[0] = "Kocaeli"

citys = ["Istanbul", "Ankara", "Izmir"]

changeCity(citys)
print(citys)  # This will print ['Kocaeli', 'Ankara', 'Izmir'] because lists are mutable
              # and the change inside the function affects the original list.

print("------------------------------------------------------------------------------")

## (*args) -> tuple
## (**args) -> dictionary

def displayUser(**args):
    for key, value in args.items():
        print(f"{key}: {value}")

displayUser(name="Kaan", age=17, city="Istanbul")
displayUser(name="Ela", age=7, city="Istanbul", country="Turkey")
displayUser(name="Ismail", age=47, city="Istanbul",phone="555-555-5555")



print("------------------------------------------------------------------------------")

word = "Python Programming"

def count(word):
    letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

print(count(word))  # This will print the count of each letter in the word "Python".

print("------------------------------------------------------------------------------")


def count(word,again):
    print(word * again)
print(count("Kaan\n", 5))  # This will print "Kaan " five times.

print("------------------------------------------------------------------------------")

my_list = []

def params(*args):
    for item in args:
        my_list.append(item)
    return my_list
print(params(1, 2, 3, "Kaan", "Ela", 3.14))  # This will print [1, 2, 3, 'Kaan', 'Ela', 3.14]

print("------------------------------------------------------------------------------")

sum_one = int(input("Enter first number: "))
sum_two = int(input("Enter second number: "))

def prime(num_one, num_two):
    for prime in range(num_one, num_two + 1):
        if prime > 1:
            for i in range(2, prime):
                if (prime % i) == 0:
                    break
            else:
                print(prime)

prime(sum_one, sum_two)  # This will print all prime numbers between the two input numbers.

print("------------------------------------------------------------------------------")

def divisors(num):
    divs = []
    for i in range(1, num + 1):
        if num % i == 0:
            divs.append(i)
    return divs
print(divisors(28))  # This will print the divisors of 28.

