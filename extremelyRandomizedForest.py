from sklearn.ensemble import ExtraTreesClassifier
import numpy as np


class extremely_randomized_trees:
    def __init__(self, X, Status):
        self.X = X
        self.Status = Status

    def feature_reduction(self):
        # Build a forest and compute the feature importances (no of trees on the forest = 250 , random seed set to 0)
        forest = ExtraTreesClassifier(n_estimators=250, random_state=0)
        forest.fit(self.X, self.Status)
        importances = forest.feature_importances_
        # for i in importances:
        #     print(i)
        indices = np.argsort(importances)[::-1]
        print(indices)
        # Print the feature ranking
        print("Feature ranking: Column names")
        for f in range(self.X.shape[1]):
            if importances[indices[f]] >= 0.05:
                print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))






