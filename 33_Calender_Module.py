import calendar

mm,dd,yyyy=map(int,input().split())
#print(list(calendar.day_name))         ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
#print(calendar.weekday(yyyy,mm,dd))    Returns the index position for the day from the calender.day_name
print(calendar.day_name[calendar.weekday(yyyy,mm,dd)].upper())