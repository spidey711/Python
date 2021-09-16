import csv, os

# .txt functions
def method_read_file(file):
    method_of_file = str(input("Read, Readline or Readlines? R or REl or RL ")).lower()
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
    else:
        print('Enter a valid option.')
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
def method_appendto_file(file):
    form = str(input("Same line or Next line: S/N: ")).lower()
    user_text = input("Enter some text: ")
    if form == 's':
        file.write(user_text)
    elif form == 'n':
        file.write(f"\n{user_text}")
    else:
        print("Please enter a valid option")
def check_encoding(file):
    print(file.encoding)
def EXIT():
    print("Okay, exiting program now...")
    exit()

path = str(input("Enter path: "))
type_of_file = str(input("Is the file text or binary or csv? t/b or c: "))
operation = str(input("What do you want to do with the file:\nRead-Write-Append (rwa)\nCheck encoding (ce)\nOPTION -> "))

# .txt conditionals 
if type_of_file == "t":
    mode = str(input("Enter mode: Read-Write-Append: r or w or a: "))
    with open(path, mode) as file:
        if mode == 'r':
            method_read_file(file)
        elif mode == 'w':
            method_write_file(file)
        elif mode == 'a':
            method_appendto_file(file)