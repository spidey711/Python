# APPEND VS EXTEND method

# Append (allows to add one more element)
li = [1,2,3,4]
li.append([1,2,3])
print(li)
# Output : [1,2,3,4,9]
# Note: the element in append() method can be an iterable too but then it will add the entire iterable as one element
li = [1,2,3,4]
li.append([5,6,7,8])
print(li)
# Output : [1,2,3,4,[5,6,7,8]]

# Extend (allows to add all elements of an iterable)
li = [1,2,3,4]
li.extend([8,9,10])
print(li)
# Output : [1,2,3,4,8,9,10]