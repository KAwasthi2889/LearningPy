month_with_30_days = [4, 6, 9, 11]
week_names = ['Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday']
def valid_date(date, month, year):
    if date <= 31 and month <= 12:
        return (date <= 28) or (month in month_with_30_days and date <= 30) or (month not in month_with_30_days and month != 2) or (check_leap(year) and date <= 29)
    else:
        return False
    
def check_leap(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)

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
    for i in month_with_30_days:
        if month > i:
            num -= 1
    return num

while True:    
    date = int(input("Enter the date: "))
    month = int(input("Enter the number of month: "))
    year = int(input("Enter the year: "))
    if valid_date(date, month, year):
        total_date = date + month_to_day(month, year) + year_to_day(year)
        weekday = total_date % 7 
        print(f"The day on {date}/{month}/{year} is {week_names[weekday]}")
        break
    else:
        print("Invalid DATE! Please enter the date again:-\n\n")