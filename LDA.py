import data
from sklearn.feature_selection import SelectFromModel
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda = LinearDiscriminantAnalysis(n_components=2)
lda = lda.fit(data.X, data.Status)

model = SelectFromModel(lda, prefit=True)
X_new = model.transform(data.X)
print(X_new.shape)

for i in range(0, 83):
    if(str(model.get_support()[i]) is "True"):
        print(str(i) + " " + str(model.get_support()[i]))



