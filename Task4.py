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


sentCalls=set() 
recivedCalls=set() 

sentTexts = set()
recivedTexts = set() 

possibleTelemarketers = set() 

for row in calls:
    # O(n)-> n where n= total number of entries in the csv
    #row[0] = sender calls, row[1] = revicer calls
    sentCalls.add(row[0])
    recivedCalls.add(row[1])

for row in texts:
    # O(n)-> n where n= total number of entries in the csv
    #row[0] = sender texts, row[1] = revicer texts
    sentTexts.add(row[0])
    recivedTexts.add(row[1])

# O(n)=n n is the number of entries in the sentCalls set 
for contact in sentCalls:
    if contact not in (recivedCalls, sentTexts, recivedCalls):
        possibleTelemarketers.add(contact)

# no duplicates because set 
possibleTelemarketers = list(sorted(possibleTelemarketers))
print ("These numbers could be telemarketers:")
print(*possibleTelemarketers, sep="\n")



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

