import pandas as pd
import csv
import matplotlib.pyplot as plt

# change the directory of data file if necessary
# same preprocessing like yellow but with chunk b/c the dataset is large
lock = 1
for chunk in pd.read_csv("yellow_tripdata_2016-04.csv", chunksize=10000):
    pd.set_option('display.max_columns', 100)

    # drop irrelevant features
    chunk = chunk.drop(['VendorID', 'store_and_fwd_flag'], axis=1)

    chunk = chunk[chunk.tpep_pickup_datetime != chunk.tpep_dropoff_datetime]
    chunk = chunk[chunk.passenger_count > 0]
    chunk = chunk[chunk.trip_distance > 0]
    chunk = chunk[chunk.pickup_longitude != 0]
    chunk = chunk[chunk.pickup_latitude != 0]
    chunk = chunk[chunk.dropoff_longitude != 0]
    chunk = chunk[chunk.dropoff_latitude != 0]

    # only keep cash and credit card because they are the most relevant
    chunk = chunk[chunk.payment_type != 3]
    chunk = chunk[chunk.payment_type != 4]
    chunk = chunk[chunk.payment_type != 5]
    chunk = chunk[chunk.payment_type != 6]

    # keep no negative value for payment
    chunk = chunk.query("extra >= 0")
    chunk = chunk.query("mta_tax >= 0")
    chunk = chunk.query("tip_amount >= 0")
    chunk = chunk.query("tolls_amount >= 0")
    chunk = chunk.query("improvement_surcharge >= 0")
    chunk = chunk.query("total_amount >= 0")

    chunk.to_csv('y04.csv', mode='a', header=lock)
    lock = 0

# show the shape of dataset
'''    checklist = ['passenger_count', 'trip_distance', 'pickup_longitude',
       'pickup_latitude', 'RatecodeID',
       'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount',
       'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
       'improvement_surcharge', 'total_amount']
    chunk.boxplot(column=[i for i in checklist], return_type='axes')
    plt.xticks(rotation=60)
    plt.ylim(-200, 200)
    plt.show()
    plt.close()'''


'''Index(['VendorID', 'tpep_pickup_datetime', 'tpep_dropoff_datetime',
       'passenger_count', 'trip_distance', 'pickup_longitude',
       'pickup_latitude', 'RatecodeID', 'store_and_fwd_flag',
       'dropoff_longitude', 'dropoff_latitude', 'payment_type', 'fare_amount',
       'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
       'improvement_surcharge', 'total_amount'],
      dtype='object')'''