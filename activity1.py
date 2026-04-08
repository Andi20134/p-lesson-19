from datetime import date, time, datetime



today = date.today()
now = datetime.now()
print("Today's date:", today)
print("\ncurrent Date and time is ", now)



print("\ndate components", today.year, today.month, today.day)