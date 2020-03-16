"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def check_dict(dict, key, duration, max_duration, max_key):
    if key in dict:
        dict[key] += duration
    else:
        dict[key] = duration

    # print(dict[key], max_duration)
    if max_duration < dict[key]:
        max_duration = dict[key]
        max_key = key

    return max_duration, max_key

number_dict = dict()
max_duration = int(calls[0][3])
max_key = calls[0][0]
for i in range(len(calls)):
    for j in range(2):
        duration = int(calls[i][3])
        max_duration, max_key = check_dict(number_dict, calls[i][j], duration, max_duration, max_key)

# for num in number_dict:
#   print(num, number_dict[num])
print(max_key, 'spent the longest time,', max_duration, 'seconds, on the phone during September 2016.')

# duration = dict()

# for row in calls:
#     duration[row[0]] = duration.get(row[0],0) + int(row[3])
#     duration[row[1]] = duration.get(row[1],0) + int(row[3])
# longestCall = ""
# maxTime = 0

# for key,value in duration.items():
#     if value > maxTime:
#         longestCall = key
#         maxTime = value

# print(longestCall + " spent the longest time, " + str(maxTime) + " seconds, on the phone during September 2016.")