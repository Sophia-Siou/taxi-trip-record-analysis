import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

#run this python file with processed dataset

# use plotly to plot geolocation
newdf = pd.DataFrame()
count = 4
while count < 7:
    # thru three monthes data, break huge data into chunks for reserving memory
    for df in pd.read_csv("dataset/g0"+str(count)+".csv", chunksize=10000):

        # keep relevant featrues
        pool = df[['Pickup_longitude', 'Pickup_latitude',
                'Dropoff_longitude', 'Dropoff_latitude']].copy()

        sampling = pool.sample(frac=0.2)
        newdf = newdf.append(sampling)


    count += 1

# commont out the other when want one of the location figure
# run this python file with processed dataset then zoom in to see the whole picture

'''fig = px.density_mapbox(df, lat='Pickup_latitude',
                                lon='Pickup_longitude', radius=5,
                                center=dict(lat=0, lon=180), zoom=0,
                                mapbox_style="stamen-terrain")
fig.show()'''

fig = px.density_mapbox(df, lat='Dropoff_latitude',
                                lon='Dropoff_longitude', radius=5,
                                center=dict(lat=0, lon=180), zoom=0,
                                mapbox_style="stamen-terrain")
fig.show()