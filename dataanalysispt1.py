import json
from pprint import pprint

#open the json file and append entries to the file
f=open('allanswers.json','r')
data=json.load(f)
print(type(data))
print(data)
f.close()

# Example of how to iterate over the list of dictionaries and pull out particular pieces of information.
ages = []
for s in range(len(data)):
    if data[s]['age'] is not '': # Catches and skips over blank entries.
        ages.append(int(data[s]['age']))

print(ages)
total = sum(ages)
average = total/len(ages)

print(average)
