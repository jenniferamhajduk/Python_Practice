current_time = list(input())
current_time = list(map(int, current_time[0] + current_time[1] + current_time[3]))
print(current_time)
hour = current_time[0] + current_time[1]
minute = current_time[3] + current_time[4]
remaining_minutes = abs(hour - minute)
print(remaining_minutes)
