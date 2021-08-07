import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
import seaborn as sns
import matplotlib.pyplot as plt

# use the preprocessed dataset to run this python file
# same process as green taxi
newdf = pd.DataFrame()
count = 4
while count < 7:
    # thru three monthes data, break huge data into chunks for reserving memory
    for chunk in pd.read_csv("dataset/y0"+str(count)+".csv", chunksize=100000):

        # keep relevant featrues
        pool = chunk[['passenger_count','trip_distance', 'extra', 'mta_tax',
                      'tip_amount','tolls_amount', 'improvement_surcharge',
                      'total_amount', 'payment_type']].copy()

        sampling = pool.sample()
        newdf = newdf.append(sampling)

    count += 1

# take out only cash cases (there is no data on credit card)
newdf = newdf.query("payment_type == 1")

X = newdf.drop('tip_amount',axis=1)
y = newdf['tip_amount']
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=0)

#________________________________________________________________#
# starting prediction

svr = SVR(kernel = 'linear', C = 1000)

sc= StandardScaler().fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)
X_test_std

svr.fit(X_train_std, y_train)
y_test_pred = svr.predict(X_test_std)
y_train_pred = svr.predict(X_train_std)

# print out error analysis stat
print("R square:" , r2_score(y_train,y_train_pred))
print("Mean Absolute error:", mean_absolute_error(y_train,y_train_pred))
print("Mean Squared Error::",  mean_squared_error(y_train,y_train_pred))


# display the fit vs actual value
plt.figure(figsize=(5, 7))
ax = sns.distplot(y, hist=False, color="r", label="Actual Value")
sns.distplot(y_test_pred, hist=False, color="b", label="Fitted Values" , ax=ax)
plt.title('Yellow Actual vs Fitted Values for tip amount')
plt.legend()
plt.savefig('Yeloow Actual vs Fitted Values for tip amount (Credit Card).png')
plt.show()
plt.close()