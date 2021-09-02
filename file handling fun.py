def method_read_file(file):

    method_of_file = str(input("Read, Readline or Readlines? R or Rel or RL ")).lower()
    
    if method_of_file == "rl":
        print(file.readlines())
    
    if method_of_file == "rel":
        num = int(input("Enter number of lines to read: "))
        count = 0
        while count <= num:
            print(file.readline())
        else:
            pass

    if method_of_file == "r":
        print(file.read())
    else:
        print("Please enter a valid option")

def method_write_file(file):

    method_of_file = str("Write or Writelines? W or WL ").lower()
    user_text = str(input("Enter some text: "))
    
    if method_of_file == "w":
        file.write(user_text)
        print("File content updated (Mode : WRITE)")

    if method_of_file == "wl":
        file.writelines(user_text)
        print("File content updated (Mode : WRITELINES)")

def EXIT():
    
    print("Okay, exiting program now...")
    exit()

mode = str(input("Enter mode: "))
path = str(input("Enter path: "))

with open(path, mode) as file:
    try:    
        
        if file.readable():
            method_read_file(path)

        else:
            print("File not readable...")
            proceed = str(input("Do you wish to update the file? Y or N")).lower()
            if proceed == "y":
                method_write_file(path)
            if proceed == "n":
                EXIT()
            else:
                print("Please enter a valid option")

    except ValueError or FileNotFoundError:
        print("Please enter the name of an existing file and give a valid mode")