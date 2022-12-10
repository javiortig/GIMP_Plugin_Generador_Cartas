import csv  
import json
 

SRC_FILE = "./descubiertos.csv"
DEST_FILE = "./web/Pokemon_web/src/data/descubiertos.js"

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

def csv_to_json(csvFile, jsonFile):    
    jsondict = []  
    with open(csvFile) as csvfile:  
        csv_data = csv.DictReader(csvfile)#Converting the csv data into dictionary
        #jsondict["data"]=[]

        for rows in csv_data:  
            print(rows)#Just for reference
            jsondict.append(rows)  #Appending all the csv rows
  

    with open(jsonFile, 'w') as jsonfile:  
        #Dumping the data into jsonfile.json
        jsonfile.write(json.dumps(jsondict, indent = 4))  #indent is used for pretty printing

    line_prepender(jsonFile, "export const pokemonDescubiertos =")

    

    
  

csv_to_json(SRC_FILE, DEST_FILE)#Calling the function