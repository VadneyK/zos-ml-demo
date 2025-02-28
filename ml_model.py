import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

class TransactionAnalyzer:
    def __init__(self):
        self.model = IsolationForest(
            contamination=0.1,
            random_state=42
        )
        self.scaler = StandardScaler()
        
    def prepare_features(self, transaction_data):
        """
        Prepare features from transaction data.
        Expected format: amount, time_of_day, transaction_type
        """
        features = np.array(transaction_data)
        return self.scaler.fit_transform(features)
        
    def train(self, transaction_data):
        """Train the anomaly detection model"""
        features = self.prepare_features(transaction_data)
        self.model.fit(features)
        
    def predict(self, transaction):
        """Predict if a transaction is anomalous"""
        features = self.scaler.transform([transaction])
        prediction = self.model.predict(features)
        return prediction[0] == 1  # 1 for normal, -1 for anomalous
        
    def save_model(self, path):
        """Save the trained model"""
        joblib.dump({
            'model': self.model,
            'scaler': self.scaler
        }, path)
        
    @classmethod
    def load_model(cls, path):
        """Load a trained model"""
        saved_data = joblib.load(path)
        instance = cls()
        instance.model = saved_data['model']
        instance.scaler = saved_data['scaler']
        return instance
