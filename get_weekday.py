def check_leap(year: int) -> int:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
            return True

def number_of_leap(year: int) -> int:
    num = 0
    for i in range(year):
        if check_leap(i):
            num += 1
    return num

def year_to_day(year: int) -> int:
    return (year * 365 + number_of_leap(year))

def month_to_day(month: int, year: int) -> int:
    num = month * 31
    if month > 2:
        if check_leap(year):
            num -= 2
        else:
            num -= 3
    month_with_30 = [4, 6, 9, 11]
    for i in month_with_30:
        if month > i:
            num -= 1
    return num
    
date = int(input("Enter the date: "))
month = int(input("Enter the number of month: "))
year = int(input("Enter the year: "))
total_date = date + month_to_day(month, year) + year_to_day(year)
weekday = total_date % 7
week_names = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday'] 
print(week_names[weekday])