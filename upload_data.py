from pymongo.mongo_client import MongoClient
import pandas as pd
import json

# uniform resource indentifier
uri = "mongodb://yashdb:yashdb9021@cluster0-shard-00-00.eax8z.mongodb.net:27017,cluster0-shard-00-01.eax8z.mongodb.net:27017,cluster0-shard-00-02.eax8z.mongodb.net:27017/?ssl=true&replicaSet=atlas-f73n6c-shard-0&authSource=admin&retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# create database name and collection name
DATABASE_NAME="craditcarddb"
COLLECTION_NAME="craditcardfault"

# read the data as a dataframe
df=pd.read_csv(r"C:\Users\Raju\OneDrive\Desktop\craditcad-fault-detection\notebooks\creditCardFraud_28011964_120214.csv")
df=df.drop("Unnamed: 0",axis=1)

# Convert the data into json
json_record=list(json.loads(df.T.to_json()).values())

#now dump the data into the database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
