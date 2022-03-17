import datetime

Year = int(input("Year : "))
days = int(input("day : "))

date = datetime.date(Year, 1, 1)
delta = datetime.timedelta(days - 1)
newdate = delta + date
newdate = str(newdate)

year, month, day = newdate.split("-")

print(day + "." + month + "." + year)