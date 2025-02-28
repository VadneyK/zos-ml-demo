"""
Machine Learning Model for Transaction Analysis
"""
import numpy as np
from sklearn.ensemble import IsolationForest

class TransactionAnalyzer:
    def __init__(self):
        self.model = IsolationForest(
            n_estimators=100,
            contamination=0.1,
            random_state=42
        )
        self.is_trained = False
        self.training_data = []

    def add_transaction(self, transaction_data):
        """Add transaction data for training."""
        self.training_data.append(transaction_data)

    def train(self):
        """Train the model on collected data."""
        if len(self.training_data) < 10:
            return False
        
        X = np.array(self.training_data)
        self.model.fit(X)
        self.is_trained = True
        return True

    def analyze(self, transaction):
        """Analyze a transaction for anomalies."""
        if not self.is_trained:
            return None
        
        X = np.array([transaction])
        score = self.model.score_samples(X)[0]
        prediction = self.model.predict(X)[0]
        
        return {
            'score': float(score),
            'is_anomaly': int(prediction) == -1,
            'confidence': float(np.exp(score) / (1 + np.exp(score)))
        }
