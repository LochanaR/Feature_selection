from sklearn.neighbors import KNeighborsClassifier
import data
from mlxtend.feature_selection import SequentialFeatureSelector as SFS
X = data.X.as_matrix(columns=None)
Status = data.Status.as_matrix(columns=None)

knn = KNeighborsClassifier(n_neighbors=4)

sfs1 = SFS(knn,k_features=5,forward=True,floating=False,scoring='accuracy',cv=0)
sfs1 = sfs1.fit(X,Status)
print(sfs1.k_feature_idx_)
print(sfs1.k_score_)