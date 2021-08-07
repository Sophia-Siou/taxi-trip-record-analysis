import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#run this python file with processed dataset
# same data gathering process as the pairwise plot
newdf = pd.DataFrame()
count = 4
while count < 7:
    # thru three monthes data, break huge data into chunks for reserving memory
    for df in pd.read_csv("dataset/y0"+str(count)+".csv", chunksize=100000):
        pd.set_option('display.max_columns', 100)

        # for feature correlation, need date difference be float type
        pick = df['tpep_pickup_datetime']
        drop = df['tpep_dropoff_datetime']
        pick = pd.to_datetime(pick)
        drop = pd.to_datetime(drop)
        minues = (drop - pick).dt.total_seconds() / 60
        df['travel_time'] = minues

        # keep relevant featrues
        pool = df[['passenger_count', 'trip_distance', 'pickup_longitude',
       'pickup_latitude', 'RatecodeID', 'dropoff_longitude',
       'dropoff_latitude', 'payment_type', 'fare_amount', 'extra', 'mta_tax',
       'tip_amount', 'tolls_amount', 'improvement_surcharge', 'total_amount',
       'travel_time']].copy()

        # sampling 20% from the data each chunk to save memory
        sampling = pool.sample()
        newdf = newdf.append(sampling)

    count += 1

# create heatmap to see the correlation between useful features
sns.heatmap(newdf.corr(), annot=True)
plt.xticks(rotation=45)
plt.savefig("yellow variable heatmap correlation.png")
plt.show()
plt.close()