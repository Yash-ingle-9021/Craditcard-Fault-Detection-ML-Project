import os


AWS_S3_BUCKET_NAME = "craditcard-fault"
MONGO_DATABASE_NAME = "craditcarddb"
MONGO_COLLECTION_NAME = "craditcardfault"

TARGET_COLUMN = "default payment next month"
MONGO_DB_URL="mongodb://yashdb:yashdb9021@cluster0-shard-00-00.eax8z.mongodb.net:27017,cluster0-shard-00-01.eax8z.mongodb.net:27017,cluster0-shard-00-02.eax8z.mongodb.net:27017/?ssl=true&replicaSet=atlas-f73n6c-shard-0&authSource=admin&retryWrites=true&w=majority"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder =  "artifacts"