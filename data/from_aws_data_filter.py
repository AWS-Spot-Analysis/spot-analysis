import pandas as pd
import time
import dateutil.parser

filename = './awsData-ap-northeast-2.csv'
outfile = "subset.csv"
#Time the opperation in milliseconds
start = time.time()

# GET Data from orginal CSV source
df = pd.read_csv(filename, header = None)

# add column names
df.columns = ["info", "AvailabilityZone","InstanceType", "SpotPrice", "TimeStamp" ]

#drop the info column
df.drop("info",axis=1, inplace=True)

# Clean the iso timestamps for translation to python datetime
df['TimeStamp'] = df['TimeStamp'].map(lambda x: str(x).replace("T", " ").rstrip('Z')) 

#Drop the first row and any row that contains the column names,
# this happens because of the concat used to create the larger file
df.drop(df.index[[0]], inplace=True)
df = df.dropna()
df = df[df.AvailabilityZone != "AvailabilityZone"]

# Convert the timestamps to python ones
df['TimeStamp'] = pd.to_datetime(df.TimeStamp)

#make the timestamp the index
df.index = df.TimeStamp

#drop the old timestamp row
df.drop('TimeStamp', axis=1, inplace=True)
df = df.truncate(before='2016-10-13 00:00:00', after='2016-12-11 00:00:00')
# create the new csv file with the filtered data
df.to_csv(outfile)
print(time.time()-start)
print("Done")