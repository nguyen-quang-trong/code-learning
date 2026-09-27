import csv 
import os

duongdan=os.path.join(os.path.dirname(__file__), "datacsv.csv")
with open(duongdan, newline='') as f: 
    reader = csv.reader(f, delimiter=';', quoting=csv.QUOTE_NONE) 
    for row in reader: 
        print(row[0],"\t",row[1]) 
