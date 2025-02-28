import numpy as np
from ml_model import TransactionAnalyzer

def test_transaction_analyzer():
    # Create sample transaction data
    transaction_data = [
        [100.0, 12.0, 1.0],  # Normal transaction
        [1000.0, 3.0, 2.0],  # Large transaction at odd hours
        [50.0, 14.0, 1.0],   # Normal transaction
        [5000.0, 2.0, 3.0],  # Very large international transaction at night
    ]
    
    # Initialize and train model
    analyzer = TransactionAnalyzer()
    analyzer.train(transaction_data)
    
    # Test normal transaction
    normal_transaction = [150.0, 13.0, 1.0]
    assert analyzer.predict(normal_transaction) == True, "Should identify normal transaction"
    
    # Test potentially anomalous transaction
    anomalous_transaction = [10000.0, 2.0, 3.0]
    result = analyzer.predict(anomalous_transaction)
    print(f"Anomalous transaction prediction: {result}")
    
if __name__ == "__main__":
    test_transaction_analyzer()
