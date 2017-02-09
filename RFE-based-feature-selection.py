from sklearn.svm import SVC
import pandas as pd
from sklearn.feature_selection import RFE
import data
# Load the dataset
# path1 = "C:\\Users\\pavilion 15\\Downloads\\times.csv"

# dataframe = pd.read_csv(path1)
X = data.X
y = data.Status


svc = SVC(kernel="linear")
print("Model created")
rfe = RFE(estimator=svc, n_features_to_select= 5)
rfe = rfe.fit(X,y)
print(rfe.support_)
print(rfe.ranking_)
