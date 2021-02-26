from datetime import datetime


def hour_min_2_mins(hour, minute):
    return((60*hour) + minute)

earlyWeek = True
if(earlyWeek):
    endHour = 15
    endMinute = 30
else:
    endHour = 16
    endMinute = 30


#currTime = datetime.now()
#print(currTime.hour, currTime.minute)
currTimehour = 10
currTimeminute = 42

endMinutes = hour_min_2_mins(endHour, endMinute)
#print(hour_min_2_mins(endHour, endMinute))
currentMinutes = hour_min_2_mins(currTimehour, currTimeminute)
#print(hour_min_2_mins(currTimehour, currTimeminute))

totalMinutesLeft = endMinutes - currentMinutes
#print(totalMinutesLeft)

hoursLeft = int(totalMinutesLeft/60)
#print(hoursLeft)
minutesLeft = totalMinutesLeft % 60
#print(minutesLeft)

