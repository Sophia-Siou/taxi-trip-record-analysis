import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly
import plotly.express as px

#run this python file with processed dataset


# plotly to plot geolocation
newdf = pd.DataFrame()
count = 4
while count < 7:
    # thru three monthes data, break huge data into chunks for reserving memory
    for df in pd.read_csv("dataset/y0"+str(count)+".csv", chunksize=100000):

        # keep relevant featrues
        pool = df[['pickup_longitude', 'pickup_latitude',
                'dropoff_longitude', 'dropoff_latitude']].copy()


        sampling = pool.sample()
        newdf = newdf.append(sampling)


    count += 1

# commont out the other when want one of the location figure
# run this python file with processed dataset then zoom in to see the whole picture


fig = px.density_mapbox(df, lat='pickup_latitude',
                                lon='pickup_longitude', radius=5,
                                center=dict(lat=0, lon=180), zoom=0,
                                mapbox_style="stamen-terrain")
fig.show()

'''fig = px.density_mapbox(df, lat='dropoff_latitude',
                                lon='dropoff_longitude', radius=5,
                                center=dict(lat=0, lon=180), zoom=0,
                                mapbox_style="stamen-terrain")
fig.show()'''