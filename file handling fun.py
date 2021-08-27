def method_read_file():
    method_of_file = str(input("Read or Readlines? R or RL")).lower()
    if method_of_file == "RL":
        print(filename.readlines())
    else:
        print(filename.read())
def EXIT():
    print("Okay, exiting program now...")
    exit()
try:
    mode = str(input("Enter mode: "))
    path = str(input("Enter path: "))
    filename = open(path, mode)
    if filename.writable() == True:
        user_text = str(input("Enter some text: "))
        filename.write(user_text)
        print("File has been edited")
    elif filename.writable() == False:
        print("File cannot be edited")
        proceed = str(input("Do you want to read the file? Y or N ")).lower()
        if proceed == 'y':
            method_read_file()
        elif proceed == "n":
            EXIT()
        else:
            print("Please enter a valid option")
    elif filename.readable() == True:
        method_read_file()
    else:
        print("File cannot be read")
except ValueError or FileNotFoundError:
    print("Please enter the name of an existing file and give a valid mode")