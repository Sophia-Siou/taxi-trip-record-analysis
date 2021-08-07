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
    for df in pd.read_csv("dataset/g0"+str(count)+".csv", chunksize=10000):
        pd.set_option('display.max_columns', 100)

        # for feature correlation, need date difference be float type
        pick = df['lpep_pickup_datetime']
        drop = df['Lpep_dropoff_datetime']
        pick = pd.to_datetime(pick)
        drop = pd.to_datetime(drop)
        minues = (drop - pick).dt.total_seconds() / 60
        df['travel_time'] = minues

        # keep relevant featrues
        pool = df[['RateCodeID', 'Pickup_longitude', 'Pickup_latitude',
                'Dropoff_longitude', 'Dropoff_latitude', 'Passenger_count',
                'Trip_distance', 'Extra', 'MTA_tax', 'Tip_amount',
                'Tolls_amount', 'improvement_surcharge', 'Total_amount', 'Payment_type',
                'Trip_type ', 'travel_time']].copy()

        sampling = pool.sample(frac=0.2)
        newdf = newdf.append(sampling)

    count += 1

# create heatmap to see the correlation between useful features
sns.heatmap(newdf.corr(), annot=True)
plt.xticks(rotation=45)
plt.savefig("green variable heatmap correlation.png")
plt.show()
plt.close()