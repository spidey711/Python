import csv, os

print("Anytime you wish to exit just say 'exit' in any of the replies...")

path = str(input("Enter path: "))
type_of_file = str(input("Is the file text or binary or csv? t/b or c: "))

# .txt and .bin functions
def method_read_file(file):
    method_of_file = str(input("Read, Readline or Readlines? r or rel or rl: ")).lower()
    if method_of_file == "rl":
        print(file.readlines())
    elif method_of_file == "rel":
        num = int(input("Enter number of lines to read: "))
        count = 0
        while True:
            if count >= num:
                print(file.readline())
            else:
                break
    elif method_of_file == 'r':
        print(file.read())
    elif method_of_file == 'exit':
        EXIT()
    else:
        print('Enter a valid option.')
def method_write_file(file):
    method_of_file = str(input("Write (W) or Writelines (WL): ")).lower()
    user_text = input("Enter some text: ")
    if method_of_file == "w":
        file.write(user_text)
        print("File Content has been updated [MODE: write]")
    elif method_of_file == "wl":
        file.writelines(user_text)
        print("File Content has been updated [MODE: writelines]")
    elif method_of_file == 'exit':
        EXIT()
    else:
        print("Please enter a valid option")
def method_appendto_file(file):
    form = str(input("Same line or Next line: S/N: ")).lower()
    user_text = input("Enter some text: ")
    if form == 's':
        file.write(user_text)
    elif form == 'n':
        file.write(f"\n{user_text}")
    elif form == 'exit':
        EXIT()
    else:
        print("Please enter a valid option")
def check_encoding(file):
    print(file.encoding)
def EXIT():
    print("Okay, exiting program now...")
    exit()

# .txt and .bin conditionals 
if type_of_file == "t/b":
    choice = str(input('Text or Binary: T or B: ')).lower()
    if choice == "t":
        mode = str(input("Enter mode: Read-Write-Append: r or w or a: "))
        with open(path, mode) as file:
            if mode == 'r':
                with open(path, 'r') as file:
                    method_read_file(file)
            elif mode == 'w':
                with open(path, 'w') as file:
                    method_read_file(file)
            elif mode == 'a':
                with open(path, 'a') as file:
                    method_read_file(file)
            elif mode == 'exit':
                EXIT()
            else:
                print("Please enter a valid option")
    elif choice == 'b':
        mode = str(input("Enter mode: Read-Write-Append: rb or wb or ab: "))
        if mode == 'rb':
            with open(path, 'rb') as file:
                method_read_file(file)
        elif mode == 'wb':
            with open(path, 'wb') as file:
                method_read_file(file)
        elif mode == 'ab':
            with open(path, 'ab') as file:
                method_read_file(file)
        elif mode == 'exit':
            EXIT()
        else:
            print("Please enter a valid option")
    else:
        print('Please enter a valid option')
elif type_of_file == 'c':
    if True:
        pass
    elif mode == 'exit':
        EXIT()
    else:
        print('Please enter a valid option')
else:
    print("Please enter a valid option")