title = input("Enter event title: ")

while True:
    try:
        year = int(input("Enter year: "))
        month = int(input("Enter month: "))
        day = int(input("Enter day: "))
        if not 1 <= year <= 2026:
            print("Year must be 1-2026.\n")
        elif not 1 <= month <= 12:
            print("Month must be 1-12.\n")
        elif not 1 <= day <= 31:
            print("Day must be 1-31.\n")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter numbers only.\n")

print()
print("Formatted Output:")
print("Event:", title.upper())
print("Date:", str(month) + "/" + str(day) + "/" + str(year))
print("Year:", year)
print("Month:", month)
print("Day:", day)