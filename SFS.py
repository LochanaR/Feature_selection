from sklearn.neighbors import KNeighborsClassifier
import data
from mlxtend.feature_selection import SequentialFeatureSelector as SFS

X = data.X.as_matrix(columns=None)
Status = data.Status.as_matrix(columns=None)

knn = KNeighborsClassifier(n_neighbors=4)
# sequential forward selection
sfs = SFS(knn, k_features=5, forward=True, floating=False, scoring='accuracy',print_progress=False, cv=0)
sfs = sfs.fit(X, Status)
print('\nSequential Forward Selection (k=5):')
print(sfs.k_feature_idx_)
print('CV score:')
print(sfs.k_score_)

# sequential backward selection
sbs = SFS(knn, k_features=5, forward=False, floating=False, scoring='accuracy', print_progress=False, cv=0)
sbs = sbs.fit(X,Status)
print('\nSequential Backward Selection (k=5):')
print(sbs.k_feature_idx_)
print('CV score:')
print(sbs.k_score_)

# sequential floating forward selection
sffs = SFS(knn, k_features=5, forward=True, floating=True, scoring='accuracy',print_progress=False, cv=0)
sffs = sffs.fit(X, Status)
print('\nSequential Floating Forward Selection (k=5):')
print(sffs.k_feature_idx_)
print('CV score:')
print(sffs.k_score_)

# sequential floating backward selection
sfbs = SFS(knn, k_features=5, forward=False, floating=True, scoring='accuracy', print_progress=False, cv=0)
sfbs = sfbs.fit(X,Status)
print('\nSequential Floating Backward Selection (k=5):')
print(sfbs.k_feature_idx_)
print('CV score:')
print(sfbs.k_score_)