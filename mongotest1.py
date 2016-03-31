import sys
import pandas as pd
import pymongo
import json
import os

def import_content(filepath, collection):
    client = pymongo.MongoClient()
    database = client['bdproj1'] # Replace mongo db name
    #collection = 'user' # Replace mongo db collection name
    db_coll = database[collection]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_coll.remove()
    #if db_coll.collection.count() == 0
    db_coll.insert(data_json)
    #else
    #	db_coll.update() # update collection with additional fields - ask Jose 

if __name__ == "__main__":
  filepath = '/Users/joannelin/Documents/BD_project1/dataset1.csv'  #pass csv file path
  import_content(filepath, 'user')
  filepath = '/Users/joannelin/Documents/BD_project1/dataset2.csv'  #pass csv file path
  import_content(filepath, 'org')
  
