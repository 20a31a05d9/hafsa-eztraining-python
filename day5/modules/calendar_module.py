import calendar as c

print('full calendar')
print(c.calendar(2022))

print('particular month')
print(c.month(2003,5))

print("set 1st day of the weeek")
c.setfirstweekday(c.FRIDAY)
print(c.month(2023,2))