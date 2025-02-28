import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/api/health', headers={'X-User-ID': 'MLAPPADM'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'status' in data
    assert data['status'] == 'healthy'

def test_analyze_transaction(client):
    transaction_data = {
        "transaction": {
            "amount": 1000.00,
            "type": "TRANSFER",
            "source_account": "SAVINGS",
            "target_account": "CHECKING",
            "timestamp": "2025-02-28T12:00:00Z"
        }
    }
    response = client.post('/api/analyze', 
                         json=transaction_data,
                         headers={'X-User-ID': 'MLAPPADM'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'analysis' in data
    assert 'risk_score' in data['analysis']

def test_performance_metrics(client):
    response = client.get('/api/performance', headers={'X-User-ID': 'MLAPPADM'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'metrics' in data
    assert 'cpu_usage' in data['metrics']

def test_security_status(client):
    response = client.get('/api/security', headers={'X-User-ID': 'MLAPPADM'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'event_analysis' in data
