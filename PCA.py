import data
from sklearn import decomposition

pca = decomposition.PCA(n_components= 50)
pca.fit(data.X)
X_new = pca.transform(data.X)