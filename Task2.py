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

sendingTelephone = []
receivingTelephone = []
timestamp = [] 
duration = [] 
phone_dict = {} 

# O(n)-> n where n = total number of entries in the csv
for row in calls:
    sendingTelephone = row[0]
    receivingTelephone = row[1] 
    duration = row[3] 
# for sender
# O(n)-> 1 to check key and set value
#dictionaries have constant time to access the record
    if sendingTelephone not in phone_dict:
        phone_dict[sendingTelephone] = int(duration)
    else:
        phone_dict[sendingTelephone] += int(duration)

# for reciever 
# O(n)-> 1 to check key and set value 
    if receivingTelephone not in phone_dict:
        phone_dict[receivingTelephone] = int(duration)
    else:
        phone_dict[receivingTelephone] += int(duration) 

highestDuration = max(phone_dict.values())
longestCaller = max(phone_dict, key= phone_dict.get)

# worst time complexity is O(n)
print("{} is the highest duration telephone for duration {}".format(longestCaller, highestDuration))
    

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

