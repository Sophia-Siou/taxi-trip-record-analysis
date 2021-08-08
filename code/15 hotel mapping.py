import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

#https://www.kaggle.com/gdberrio/new-york-hotels

newdf = pd.DataFrame()

# thru three monthes data, break huge data into chunks for reserving memory
df = pd.read_csv("hotel.csv", encoding='cp1252')

# keep relevant featrues for pairwise analysis
newdf = df[['latitude', 'longitude', 'star_rating',
            'low_rate', 'high_rate']].copy()

# only see five stars b/c we're focusing on luxury comsumption people
newdf = newdf.query("star_rating == 5")
#newdf = newdf.nlargest(300, 'star_rating')
#newdf = newdf.nlargest(300, 'high_rate')

print(newdf)

fig = px.density_mapbox(newdf, lat='latitude',
                                lon='longitude', z='star_rating',
                                radius=5,center=dict(lat=0, lon=180), zoom=0,
                                mapbox_style="stamen-terrain")
fig.show()
