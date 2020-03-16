"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def check_dict(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

number_dict = dict()
for i in range(len(texts)):
    for j in range(2):
        check_dict(number_dict, texts[i][j])
for i in range(len(calls)):
    for j in range(2):
        check_dict(number_dict, calls[i][j])
# for key in number_dict:
#     print(key)
print('There are', len(number_dict) ,'different telephone numbers in the records.')