import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#run this python file with processed dataset
newdf = pd.DataFrame()
count = 4
while count < 7:
    # thru three monthes data, break huge data into chunks for reserving memory
    for df in pd.read_csv("dataset/y0"+str(count)+".csv", chunksize=100000):
        pd.set_option('display.max_columns', 100)

        # for feature correlation, need date difference be float type
        # so convert the date time to mintues that have been traveled
        pick = df['tpep_pickup_datetime']
        drop = df['tpep_dropoff_datetime']
        pick = pd.to_datetime(pick)
        drop = pd.to_datetime(drop)
        minues = (drop - pick).dt.total_seconds() / 60
        df['travel_time'] = minues

        # keep relevant featrues for pairwise analysis
        pool = df[['passenger_count','trip_distance',
                   'tip_amount', 'payment_type', 'travel_time']].copy()

        sampling = pool.sample()
        newdf = newdf.append(sampling)

    count += 1

# plot the pairwise graph, comment the one out when doing the other
sns.pairplot(newdf, hue='Payment_type', kind='kde')
#sns.pairplot(newdf, hue='Payment_type')
plt.savefig('yellow pairwise kde.png')
plt.show()
plt.close()


