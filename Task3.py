"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

sendingTelephone = []
receivingTelephone = []
# timestamp = [] 
# duration = [] 

# initializing for PartA 
areaCodes = [] 
# initializing for Part B
revivedCalls = [] 
countOfSentCalls = 0
for row in calls:
    sendingTelephone = row[0]
    receivingTelephone = row[1] 
    # print(receivingTelephone)
    if sendingTelephone.startswith('(080'):
      countOfSentCalls+=1
      if receivingTelephone.startswith('(0'):
        # O(n) where n = length of string 
        fixedLine = receivingTelephone[0:receivingTelephone.find(')')+1]
        revivedCalls.append(fixedLine)
        areaCodes.append(fixedLine)
        # print("{} fixed area code".format(areaCode)) 
        # break
      if receivingTelephone.startswith(('7', '8', '9')):
        # O(n) where n = length of string 
        mobileLine = receivingTelephone[0:4]
        areaCodes.append(mobileLine)

      if receivingTelephone.startswith('140'):
        # O(n) where n = length of string 
        telemarketerLine = '140'
        areaCodes.append(telemarketerLine)

# PART - A
# sorting -- O(n)= n*logn

areaCodes = list(set(sorted(areaCodes)))
print("The numbers called by people in Bangalore have codes:") 
# * operator helps separate content by space 
print(*areaCodes, sep='\n')


# PART - B
# O(n) = 1 - constant as it is arithmatic operation 
revivedCalls = len(revivedCalls)
# print(revivedCalls)
# print(countOfSentCalls)
percentage = (revivedCalls/countOfSentCalls)*100
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore".format(percentage))



      







"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
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
