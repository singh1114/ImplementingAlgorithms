# first import the library that handles the calendar functon
import calendar

print('Enter the year whose calendar you want to see\n')
year = raw_input()

print(calendar.calendar(int(year)))
