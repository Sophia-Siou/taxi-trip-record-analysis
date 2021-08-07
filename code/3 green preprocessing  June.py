import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt

# change the directory of file if necessary
df = pd.read_csv("green_tripdata_2016-06.csv")
pd.set_option('display.max_columns', 100)

'''
these are the columns in dataset that have been read
Index(['VendorID', 'lpep_pickup_datetime', 'Lpep_dropoff_datetime',
       'Store_and_fwd_flag', 'RateCodeID', 'Pickup_longitude',
       'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude',
       'Passenger_count', 'Trip_distance', 'Fare_amount', 'Extra', 'MTA_tax',
       'Tip_amount', 'Tolls_amount', 'Ehail_fee', 'improvement_surcharge',
       'Total_amount', 'Payment_type', 'Trip_type '],
      dtype='object')
'''
# drop irrelevant features
df = df.drop(['VendorID', 'Store_and_fwd_flag', 'Fare_amount', 'Ehail_fee'], axis=1)

# see if there is any missing value by peaking the statistic summary
# find out if there is any missing value or outliers
#print(df.describe())

# below are the attributes shouldn't have 0 (which includes missing val), so del those rows
df = df[df.lpep_pickup_datetime  != df.Lpep_dropoff_datetime]
df = df[df.Pickup_longitude  != 0]
df = df[df.Pickup_latitude  != 0]
df = df[df.Dropoff_longitude  != 0]
df = df[df.Dropoff_latitude  != 0]
df = df[df.Passenger_count  > 0]
df = df[df.Trip_distance > 0]

# only keep cash and credit card because they are the most relevant
df = df[df.Payment_type != 3]
df = df[df.Payment_type != 4]
df = df[df.Payment_type != 5]
df = df[df.Payment_type != 6]

# keep no negative value for payment
df = df.query("Extra >= 0")
df = df.query("MTA_tax >= 0")
df = df.query("Tip_amount >= 0")
df = df.query("Tolls_amount >= 0")
df = df.query("improvement_surcharge >= 0")
df = df.query("Total_amount >= 0")

'''print(df.describe())
print(df.shape)'''

# output the processed dataset
df.to_csv('g06.csv')

'''# plot the shape of dataset as boxplot
checklist = ['Pickup_longitude', 'Pickup_latitude', 'Dropoff_longitude', 'Dropoff_latitude',
       'Passenger_count', 'Trip_distance', 'Extra', 'MTA_tax',
       'Tip_amount', 'Tolls_amount', 'improvement_surcharge',
       'Total_amount', 'Payment_type']
df.boxplot(column=[i for i in checklist], return_type='axes', figsize=(20, 20))
plt.xticks(rotation=60)
plt.ylim(-200,200)
plt.savefig("attribute g06.png")
plt.show()
plt.close()'''