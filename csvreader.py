#! python3
# csvreader.py
# working directory

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

#Looping through every file in the current working directory

for csvFilename in os.listdir('.'):
    if not csvFilename.endswith('.csv'):
        continue # skip non-csv files


    print('Removing header from ' + csvFilename + '...')

    # To do: Read the csv file in (skipping first row).
    #To do: Write out the csv fileself.


csvRows = []
csvFileObj = open(example.csv)
readerObj = csv.reader.(csvFileObj)
for row in readerObj:
    if readerObj.line_num == 1:
        continue
    csvRows.append(row)

csvFileObj.close()

csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w',
newline='')
csvWriter = csv.writer(csvFileOnj)
for row in csvRows:
    csvWriter.writerow(row)
csvFileObj.close()
