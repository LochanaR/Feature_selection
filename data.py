import pandas as pd

#location for data set
path = "C:/Users/pavilion 15/PycharmProjects/FeatureReduction/Files/ME-1 Thread Freeze/ME-1.csv"
# path = "C:/Users/pavilion 15/PycharmProjects/FeatureReduction/Files/NG-1 Real Thread Freeze/NG-1.csv"
# path = "C:/Users/pavilion 15/PycharmProjects/FeatureReduction/Files/NG-2 Kill Start/NG-2.csv"
# path = "C:/Users/pavilion 15/PycharmProjects/FeatureReduction/Files/SEQ-1 IO/SEQ-1.csv"

dataframe = pd.read_csv(path)
no_of_cols = len(dataframe.columns.values)
print(no_of_cols)
# timestamp column will not be considered in the feature selection
X = dataframe.ix[:, 1:no_of_cols-1]
print(X.columns.values)
print(X.shape)
Status = dataframe.ix[:, no_of_cols-1:no_of_cols]
print(Status.columns.values)
print(Status.shape)

