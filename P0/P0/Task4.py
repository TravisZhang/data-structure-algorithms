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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def check_dict(dict, key):
    if key in dict:
        dict[key] += 1
    else:
        dict[key] = 1

# they might use a non-telemarketer number, so no need for '140' check
def check_caller_dict(texter_dict, caller_dict, listerner_dict, marketer_dict):
    for key in caller_dict:
        if (not (key in texter_dict or key in listerner_dict)):
        # if ((not key in texter_dict) and (not key in listerner_dict)):
            marketer_dict[key] = caller_dict[key]

def sort_order(key):
    if key[0] != '(':
        return int(key[0])
    else:
        return int(key[2]) + 10

caller_dict = dict()
listerner_dict = dict()
texter_dict = dict()
marketer_dict = dict()
for i in range(len(texts)):
    for j in range(2):
        check_dict(texter_dict, texts[i][j])
for i in range(len(calls)):
    check_dict(caller_dict, calls[i][0])
    check_dict(listerner_dict, calls[i][1])

check_caller_dict(texter_dict, caller_dict, listerner_dict, marketer_dict)
# print(marketer_dict)
# print(len(marketer_dict))
# sorted(marketer_dict.keys(), key = sort_order)
# sorted(marketer_dict.items())
# [(k,marketer_dict[k]) for k in sorted(marketer_dict.keys())] 
print('These numbers could be telemarketers: ')
# for num in marketer_dict:
#     print(num)

# print(sorted(marketer_dict.items(), key=lambda d: d[0])) 
# print(sorted(marketer_dict.keys(), key = sort_order))
print(* sorted(marketer_dict.keys()), sep = '\n')
