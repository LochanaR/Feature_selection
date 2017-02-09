import extremelyRandomizedForest
import data
forest_reduction = extremelyRandomizedForest.extremely_randomized_trees(data.X, data.Status)
forest_reduction.feature_reduction()


