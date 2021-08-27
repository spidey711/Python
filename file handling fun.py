def method_read_file():
    method_of_file = str(input("Read or Readlines? R or RL")).lower()
    if method_of_file == "RL":
        print(filename.readlines())
    else:
        print(filename.read())
def EXIT():
    print("Okay, exiting program now...")
    exit()
mode = str(input("Enter mode: "))
path = str(input("Enter path: "))
filename = open(path, mode)
if filename.writable() == True:
    user_text = str(input("Enter some text: "))
    filename.write()
    print("File has been edited")
    print(filename.read())
if filename.writable() == False:
    print("File cannot be edited")
    proceed = str(input("Do you want to read the file? Y or N")).lower()
    if proceed == 'Y':
        method_read_file()
    if proceed == "N":
        EXIT()
    else:
        print("Please enter a valid option")
if filename.readable() == True:
    method_read_file()
else:
    print("File cannot be read")
    