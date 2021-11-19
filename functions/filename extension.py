# Write a Python program to accept a filename from the user and print the extension of that
def fileExtenstion():
    filename = input("Enter filename: ")
    extension = filename.split(".")
    return "Extension: {}".format(repr(extension[-1]))