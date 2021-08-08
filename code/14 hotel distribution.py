import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("hotel.csv", encoding='cp1252')
newdf = df[['latitude', 'longitude', 'star_rating',
            'low_rate', 'high_rate']].copy()

sns.histplot(data=newdf, x="high_rate", hue="star_rating")
plt.savefig('high rate by star rating.png')
plt.show()
plt.close()