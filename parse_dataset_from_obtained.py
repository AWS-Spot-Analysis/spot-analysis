import pandas as pd
import numpy
import os


rootdir = 'aws-spot-price-history'


def parse(filename):
    df = pd.read_csv(filename, sep="\t", header = None)
    df.columns = ["info", "SpotPrice", "TimeStamp", "InstanceType", "OS type", "AvailabilityZone"]
    df['TimeStamp'] =pd.to_datetime(df.TimeStamp)

    df.index = df.TimeStamp
    df = df.drop(['TimeStamp'],axis=1).drop('info', 1).sort_index()

    df1 = df[df.AvailabilityZone == 'us-west-1a']
    df2 = df1[df1.InstanceType == 'c3.8xlarge']
    with open('us-east-1a_c3-8xlarge.csv', 'a') as f:
        df.to_csv(f)


for files in os.walk(rootdir):
    for filename in files:
        #print(filename)
        try:
            parse(filename)
        except:
            pass
# parse the data file and extra the results
#filename = '/data-1397804701'
