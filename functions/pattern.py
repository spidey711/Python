# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
def pattern():
    for i in range(1, 6):
        return '*'*i
    for i in range(4, 0, -1):
        return '*'*i

print(pattern())