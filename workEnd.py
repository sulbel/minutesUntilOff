from datetime import datetime


# TO-DO: error-checking
def hour_min_2_mins(hour, minute):
    return((60*hour) + minute)

# TO-DO: way to toggle earlyWeek bool
earlyWeek = True
if(earlyWeek):
    endHour = 15
    endMinute = 30
else:
    endHour = 16
    endMinute = 30

# Print statements commented out are for debugging
currTime = datetime.now()
#print(currTime.hour, currTime.minute)
#currTimehour = 10
#currTimeminute = 42

endMinutes = hour_min_2_mins(endHour, endMinute)
#print(hour_min_2_mins(endHour, endMinute))
currentMinutes = hour_min_2_mins(currTime.hour, currTime.minute)
#print(hour_min_2_mins(currTime.hour, currTime.minute))

totalMinutesLeft = endMinutes - currentMinutes
#print(totalMinutesLeft)
hoursLeft = int(totalMinutesLeft/60)
#print(hoursLeft)
minutesLeft = totalMinutesLeft % 60
#print(minutesLeft)

print("There are:", totalMinutesLeft, "total minutes of work left.")
print("You can clock out in", hoursLeft, "hours and", minutesLeft, "minutes.\n")
