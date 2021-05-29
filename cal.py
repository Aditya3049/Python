import calendar
yy=int(input("enter an year:\n"))
if calendar.isleap(yy):
    print("year is a leap year")
else:
    print("year is not a leap year")    
