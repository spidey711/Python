# Give input out statements with the help of sys module

import sys

sys.stdout.write("Enter a number: ")
num = int(sys.stdin.readline())
print(f"User number: {num}")

# Output
# Enter a number: 12
# User number: 12