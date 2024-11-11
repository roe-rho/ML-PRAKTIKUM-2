# knn_model.py
#mohammed
from sklearn.neighbors import KNeighborsClassifier

class KNNModel:
    def __init__(self, n_neighbors=5):
        self.knn = KNeighborsClassifier(n_neighbors=n_neighbors)
        self.y_pred = None
        self.y_test = None

    def train(self, X_train, y_train):
        # Train the KNN model
        self.knn.fit(X_train, y_train)
#eugfeufeihfegfuefigegfegfiegfgeifiehgfiegfgiegef
    def predict(self, X_test):
        # Make predictions
        self.y_pred = self.knn.predict(X_test)
        return self.y_pred