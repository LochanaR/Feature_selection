import data
from  sklearn.feature_selection import SelectKBest,f_regression
from sklearn.feature_selection import chi2

model = SelectKBest(f_regression, k =10).fit(data.X, data.Status) #k is number of top features

# print(X_new.shape)


