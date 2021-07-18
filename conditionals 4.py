# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged


def string_conditional(string):
    if string.startswith('is'):
        print(string)
    else:
        # return 'Is' + string
        print('Is ' + string)

string = str(input("Enter a sentence: ")).lower()
res = string_conditional(string)
print(res)