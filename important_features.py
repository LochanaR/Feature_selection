class ImportantFeatures:
    def __init__(self):
        self.feature_set = []
    def add_features(self, feature):
        self.feature_set.append(feature)
    def display_feature_set(self):
        print(self.feature_set)


d = ImportantFeatures()
d.add_features('23')
d.add_features('34')
d.display_feature_set()