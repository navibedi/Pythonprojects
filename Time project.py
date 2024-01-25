#This is a automate greeting program where the program will look at the current time and will greet according to it
import time

actual_time= time.strftime('%H:%M:%S') #This variable is used to set the format of time in H/M/S

h=int(time.strftime('%H')) #'h' is set as the hour number

#this is a conditional statement:
if h < 12: #if the time is less then 12pm, greet good morning
   print('Good Morning')
elif h > 12 and h < 16: #if the time is in between 12pm and 4pm, greet good afternoon
    print("Good Afternoon")
elif h > 16 and h < 20: #if the time is in between 4pm and 8pm, greet good evening
    print("Good Evening")
else: #from 8 pm onwards greet good night
    print("Good Night")
