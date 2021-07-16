# Write a Python program to print the calendar of a given month and year.

import calendar

year = int(input("Enter year: "))
month = int(input("Enter month: "))

print(calendar.month(year, month))