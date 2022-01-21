"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    totalPhoneRecords = 0 
    reader = csv.reader(f)
    texts = list(reader)

unique_tele_nums = set() 
# O(n)-> n where n= total number of entries in the csv
for row in texts:
    unique_tele_nums.add(row[0])
    unique_tele_nums.add(row[1])
       
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


# O(n)-> N where N= total number of entries in the csv
for row in calls:
    unique_tele_nums.add(row[0])
    unique_tele_nums.add(row[1])
    
totalCount = len(unique_tele_nums)
print("There are {} different telephone numbers in the records.".format(totalCount))

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

