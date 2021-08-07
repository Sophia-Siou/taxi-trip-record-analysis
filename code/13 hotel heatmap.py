import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("hotel.csv", encoding='cp1252')
pd.set_option('display.max_columns', 100)

# drop the irrelevant features (star rating take service, rooms etc into account
#                                  other than location so delete)
df = df.drop(['ean_hotel_id', 'name', 'address1', 'city', 'state_province',
              'postal_code'], axis=1)

df = df[df.low_rate != 0]

# create heatmap to see the correlation between useful features
sns.heatmap(df.corr(), annot=True)
plt.xticks(rotation=45)
#plt.savefig("hotel variable heatmap correlation.png")
plt.show()
plt.close()