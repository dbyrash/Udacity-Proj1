"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
# initializing for columns 
sendingTexts = 0
receivingTexts = 1
timestampTexts = 2 
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    # O(n)-> 1 to get one element 
    textRecord = texts[0]
    
print("First record of texts, {} texts {} at time {}".format(textRecord[sendingTexts], textRecord[receivingTexts], textRecord[timestampTexts]))

#initializing for columns 
sendingTelephone = 0
receivingTelephone = 1
timestamp = 2
duration = 3
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    # O(n)-> 1 to get one element 
    callRecord = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(callRecord[sendingTelephone], \
callRecord[receivingTelephone], callRecord[timestamp], callRecord[duration]))


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

