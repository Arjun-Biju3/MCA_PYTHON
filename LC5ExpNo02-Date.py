import time
from datetime import datetime

current_date_time = datetime.now()
print(" Current date and time:", current_date_time)

current_year = current_date_time.year
print(" Current Year:" ,current_year)

month_of_year = current_date_time.strftime("%B")
print("Month of the year:", month_of_year)

week_number = current_date_time.strftime("%U")
print("Week number of the year: ",week_number)

weekday = current_date_time.strftime("%A")
print("Weekday of the week:", weekday)

day_of_year = current_date_time.timetuple().tm_yday
print("Day of year:" ,day_of_year)

day_of_month = current_date_time.day
print("Day of the month:", day_of_month)

day_of_week = current_date_time.strftime("%w")
print("Day of week:", day_of_week)
