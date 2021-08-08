import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
import plotly.graph_objects as go

# since the feature of yellow is similiar to green taxi, using the green as representive
# use the preprocessed dataset to run this python file
newdf = pd.DataFrame()
count = 4
while count < 7:
    # thru three monthes data, break huge data into chunks for reserving memory
    for chunk in pd.read_csv("dataset/g0"+str(count)+".csv", chunksize=10000):

        # keep relevant featrues for pairwise analysis
        pool = chunk[['RateCodeID', 'Pickup_longitude', 'Pickup_latitude',
       'Dropoff_longitude', 'Dropoff_latitude', 'Passenger_count',
       'Trip_distance', 'Extra', 'MTA_tax', 'Tip_amount',
       'Tolls_amount', 'improvement_surcharge', 'Total_amount', 'Payment_type',
       'Trip_type ']].copy()

        # sampling 20% from the data each chunk to save memory
        sampling = pool.sample()
        newdf = newdf.append(sampling)

    count += 1

# since looking for ppl willing to pay high tips, tip is the goal we need to predict
X = newdf.drop('Tip_amount', axis=1)
y= newdf['Tip_amount']

# use lasso to help the regression more precise
lasso = Lasso()
lasso.fit(X, y)

# perform feature selection visualization
kept_cols = [feature for feature, weight in zip(X.columns.values, lasso.coef_) if weight != 0]
figt = go.Figure(
         go.Waterfall(name= "Lasso Coefficients",
                      orientation= "h",
                      y = X.columns.values,
                      x = lasso.coef_))

figt.update_layout(title = "Coefficients of Lasso Regression Model")

figt.show()
