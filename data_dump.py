import pymongo
import pandas as pd
import json

# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

Data_file_path="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
Collection_NAME="sensor"

if __name__=="__main__":
    df=pd.read_csv(Data_file_path)
    print(f"rows and column:  {df.shape}")
    #converting json to dump in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])
 
    #insert converted jsn record to mongo db
    client[DATABASE_NAME][Collection_NAME].insert_many(json_record)

