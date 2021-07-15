# Write a Python program to accept a filename from the user and print the extension of that

filename = input("Enter filename: ")
extension = filename.split(".")
print("Extension: {}".format(repr(extension[-1])))