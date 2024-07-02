import numpy as np
from sklearn.ensemble import IsolationForest

class BehavioralAnalysis:
    def __init__(self, training_data):
        self.model = IsolationForest(contamination=0.1)
        self.model.fit(training_data)

    def detect_anomalies(self, new_data):
        return self.model.predict(new_data)
