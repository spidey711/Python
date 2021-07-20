# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# Test Data :
# Expected Output :
# {'Black', 'White'}

def color_lists(color_list_1, color_list_2):
    print(color_list_1.difference(color_list_2))

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
res = color_lists(color_list_1, color_list_2)
print(res)