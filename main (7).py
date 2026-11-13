from datetime import date

title = input("Enter event title: ")

while True:
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        if not 1 <= year <= 2026:
            print("Year must be 1-2026.\n")
            continue
        deadline = date(year, month, day)
        break
    except ValueError:
        print("Invalid date. Month must be 1-12 and day must be valid for that month.\n")

print()
print("Formatted Output:")
print("Event:", title.upper())
print(f"Date: {deadline.strftime('%B')} {deadline.day}, {deadline.year}")
print("Year:", deadline.year)
print("Month:", deadline.strftime("%B"))
print("Day:", deadline.day)
print("Weekday:", deadline.strftime("%A"))