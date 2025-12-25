
 # try except block to handle FileExistsError
# file = open("newfile3.txt", "x",encoding="utf-8")  # 

    # "r" mode is used to read data from an existing file.
try:
    file = open("newfile3.txt", "r",encoding="utf-8") 
except FileNotFoundError:
    print("File not found. Please check the file path.")

    # for loop to read file line by line
file = open("newfile.txt", "r",encoding="utf-8")

for i in file:
    print(i, end="")     # end="" to avoid double new lines








file.close()
        



