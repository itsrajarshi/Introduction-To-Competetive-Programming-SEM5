#program which gets current time and gives output of what interval it is in.
#if time is 11:19 it should give output as 11:15
#round the value of time if < 15 round to 10 if > 15 round to 20

#give user the option to take input of what they want to round to example to 4 or 5 minutes user input.
#required least time complexity and space complexity
#use readable code and comments and full names 
import time
def round_time_to_nearest_interval(current_time, interval):
    # Convert current time to minutes
    total_minutes = current_time.tm_hour * 60 + current_time.tm_min
    
    # Round to the nearest interval
    rounded_minutes = round(total_minutes / interval) * interval
    
    # Convert back to hours and minutes
    rounded_hours = rounded_minutes // 60
    rounded_minutes = rounded_minutes % 60
    
    return rounded_hours, rounded_minutes

current_time = time.localtime()
interval = int(input("Enter the interval in minutes to round to (e.g., 4 or 5): "))
rounded_time = round_time_to_nearest_interval(current_time, interval)
print("Current time:", current_time.tm_hour, ":", current_time.tm_min)
print("Rounded time:", rounded_time[0], ":", rounded_time[1])
