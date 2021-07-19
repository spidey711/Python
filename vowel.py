# Write a Python program to test whether a passed letter is a vowel or not

def check_vowel(letter):
    vowels = 'aeiou'
    return letter in vowels

letter = str(input("Enter a letter: "))
res = check_vowel(letter)
print(res)