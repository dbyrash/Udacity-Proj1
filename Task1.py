"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    totalPhoneRecords = 0 
    reader = csv.reader(f)
    texts = list(reader)

sendingTexts = []
receivingTexts = []
timestampTexts = [] 
# O(n)-> n where n= total number of entries in the csv
for row in texts:
    sendingTexts.append(row[0])
    receivingTexts.append(row[1])
    timestampTexts.append(row[2])    
countSendingTelephone = len(set(sendingTexts))
print(countSendingTelephone)
countReceivingTelephone = len(set(receivingTexts))
print(countReceivingTelephone)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

sendingTelephone = []
receivingTelephone = []
timestamp = [] 
duration = [] 
# O(n)-> N where N= total number of entries in the csv
for row in calls:
    sendingTelephone.append(row[0])
    receivingTelephone.append(row[1])
    timestamp.append(row[2])    
    duration.append(row[3])
    
countSendingTelephone = len(set(sendingTelephone))
print(countSendingTelephone)
countReceivingTelephone = len(set(receivingTelephone))
print(countReceivingTelephone)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
