def leap_check(year: int) -> bool:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        return True
year = int(input("Enter the year: "))
if leap_check(year):
    print("Year", year, "is a leap year")
else:
    print("Year", year, "is not a leap year")