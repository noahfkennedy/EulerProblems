# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# Problem 19

totalDays = 0
Sundays = 0
for year in range(1901, 2001):
    leapYear = ((year % 4 == 0) or (year % 400 == 0))
    for month in range(1, 13): 
        monthDays = 31
        if (month == 4 or month == 6 or month == 9 or month == 11):
            monthDays = 30
        elif (month == 2 and leapYear):
            monthDays = 29
        elif (month == 2 and leapYear != True):
            monthDays = 28
        
        totalDays += monthDays
        if ((totalDays - 1) % 7 == 0) and (year > 1901 and year < 2001):
            Sundays += 1
print(Sundays)

    
