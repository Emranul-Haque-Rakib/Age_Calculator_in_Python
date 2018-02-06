
import datetime


birthDate = input("Enter your birth date (dd/mm/yyyy)\n")
birthDate = datetime.datetime.strptime(birthDate, "%d/%m/%Y").date()

currentDate = datetime.datetime.today().date()

age = int(currentDate.year - birthDate.year)
month = int(currentDate.month - birthDate.month)
date = int(currentDate.day - birthDate.day)


if month < 0:
    age = age - 1
elif date < 0 and month == 0:
    age = age - 1

print("Your age is {0:d}".format(age))