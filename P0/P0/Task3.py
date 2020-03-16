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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def check_dict_inside(dict, key):
  if key in dict:
    dict[key] += 1
  else:
    dict[key] = 1

def check_dict_prefix(dict, key0, key1):
  if key0[0:5] == '(080)':
    if key1[0:2] == '(0':
      length = 3
      for i in range(2, len(key1)):
        if key1[i] == ')':
          length = i+1
          break
      code = key1[1:length-1]
      check_dict_inside(dict, code)
    elif (key1[0] == '7') or (key1[0] == '8') or (key1[0] == '9'):
      flag = 0
      for i in range(0, len(key1)):
        if key1[i] == ' ':
          flag = 1
          break
      if flag == 1:
        code = key1[0:4]
        check_dict_inside(dict, code)
    elif key1[0:3] == '140':
      code = key1[0:3]
      check_dict_inside(dict, code)

# code = calls[1194][1][0:5]
# print(code)
# print(code == '(080)')
number_dict = dict()
both_fixed_dict = dict()
prefix_dict = dict()

for i in range(len(calls)):
  check_dict_prefix(prefix_dict, calls[i][0], calls[i][1])

# prefix_dict.keys().sort()
print('The numbers called by people in Bangalore have codes:')
# for num in prefix_dict:
#   print(num)
# print(sorted(prefix_dict))
print(* sorted(prefix_dict), sep='\n')
per = 100.0 * prefix_dict['080'] / sum(prefix_dict.values())
print('%.2f percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.' % per)