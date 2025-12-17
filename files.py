    # "w" mode is used to create a new file or overwrite an existing file.
file = open("newFile.txt", "w")
    # Write some text to the file
file.write("This is a new file created using Python.\n")
file.write("This file contains multiple lines of text.\n")
file.close()            # closing the file after writing
   
    # Open the file for reading
file = open("newFile.txt", "r")
    # Read the contents of the file
content = file.read()
print("File Content:")
print(content)
file.close()            # closing the file after reading

file = open("newfile.txt", "w",encoding="utf-8")  # Firsthand information is deleted when opened in write mode
file.write("Ela Sütdonduran\n")      
file.write("Kaan Sütdonduran\n")    
file.close()

    # "a" mode is used to append data to an existing file.
file = open("newfile.txt", "a",encoding="utf-8")  # Data is added to the end of the file when opened in append mode
file.write("İsmail Sütdonduran\n")
file.close()

    # "x" mode is used to create a new file, and it raises an error if the file already exists.
#file = open("newfile2.txt", "x",encoding="utf-8")  # Creates a new file
#file.close()

   



