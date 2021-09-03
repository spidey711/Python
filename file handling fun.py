def method_read_file(file):

    method_of_file = str(input("Read, Readline or Readlines? R or REl or RL ")).lower()
    
    if method_of_file == "rl":
        print(file.readlines())
    
    elif method_of_file == "rel":
        num = int(input("Enter number of lines to read: "))
        count = 0
        while count <= num:
            print(file.readline())
        else:
            pass

    else:
        print(file.read())

def method_write_file(file):

    method_of_file = str(input("Write (W) or Writelines (WL): ")).lower()
    user_text = input("Enter some text: ")

    if method_of_file == "w":
        file.write(user_text)
        print("File Content has been updated....[MODE: write]")

    elif method_of_file == "wl":
        file.writelines(user_text)
        print("File Content has been updated....[MODE: writelines]")
    
    else:
        print("Please enter a valid option")

def check_encoding(file):
    
    print(file.encoding)

def EXIT():
    
    print("Okay, exiting program now...")
    exit()

path = str(input("Enter path: "))
operation = str(input("What do you want to do with the file:\nRead-Write (rw)\nCheck encoding (ce)\nOPTION: "))

if operation == "rw":
    
    mode = str(input("Enter mode: "))
    file = open(path, mode)
    try:    

        if file.readable():
            method_read_file(file)
        
        elif file.writable():
            method_write_file(file)

        elif not file.readable():
            print("File not readable...")
            proceed = str(input("Do you wish to update the file? Y or N ")).lower()
            file = open(path, "w")

            if proceed == "y":
                method_write_file(file)
            
            elif proceed == "n":
                EXIT()
            
            else:
                print("Please enter a valid option")
        
        elif not file.writable():
            print("File not readable...")
            
            proceed = str(input("Do you wish to update the file? Y or N ")).lower()
            file = open(path, "r")

            if proceed == "y":
                method_read_file(file)
            
            elif proceed == "n":
                EXIT()
            
            else:
                print("Please enter a valid option")
        
        else:
            EXIT()

    except ValueError or FileNotFoundError:
        print("Please enter the name of an existing file and give a valid mode")

elif operation == "ce":
    
    mode = str(input("Read or Write: R or W: "))
    file = open(path, mode) # does not matter if its r or w as encoding for both modes show same results
    check_encoding(file)

else:
    print("Please enter a valid option")