#11.Write a python program to get next day of given date using if-elif-else

year = int(input("Input a year: "))

if year % 400 == 0:
    leap_year: bool = True
elif year % 100 == 0:
    leap_year: bool = False
elif year % 4 == 0:
    leap_year: bool = True
else:
    leap_year: bool = False

month: int = int(input("Input a month [1-12]: "))

if month in (1, 3, 5, 7, 8, 10, 12):
    month_length: int = 31
elif month == 2:
    if leap_year:
        month_length: int = 29
    else:
        month_length: int = 28
else:
    month_length: int = 30


day: int = int(input("Input a day [1-31]: "))

if day < month_length:
    day += 1
else:
    day: int = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date is [dd-mm-yyyy] %d-%d-%d." % (day,  month, year ))
