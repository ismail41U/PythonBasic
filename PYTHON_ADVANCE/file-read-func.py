with open("newfile2.txt", "r",encoding="utf-8") as file: # with statement to auto close file
    content = file.read()
    print(content)
    print(file.tell())  # Get the current position of the file pointer
    file.seek(0)  # Move the file pointer back to the beginning
    print(file.tell())  # Verify the position is at the start
