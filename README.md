# z/OS Machine Learning Transaction Analyzer

A comprehensive machine learning application designed for z/OS environments, focusing on transaction pattern analysis, anomaly detection, and system monitoring.

## 🌟 Features

### 1. Transaction Analysis
- Real-time transaction pattern detection using Isolation Forest
- Risk scoring and anomaly detection
- Integration with z/OS subsystems (DB2, IMS, CICS, MQ)
- VSAM quick lookup storage

### 2. Performance Management
- Real-time system metrics monitoring
- CPU, memory, and I/O metrics collection
- Performance trend analysis
- Resource utilization tracking
- Automated recommendations

### 3. Security Features
- RACF permission verification
- Comprehensive security auditing
- Suspicious pattern detection
- Security event logging
- Detailed security reporting
- Automated security scanning with Bandit

### 4. System Integration
- DB2 transaction storage
- IMS transaction processing
- CICS transaction handling
- MQ asynchronous processing
- System Automation
- Parallel Sysplex support

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- z/OS environment
- Required Python packages (see pyproject.toml)

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd zos-ml-demo
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Unix/macOS
venv\Scripts\activate     # On Windows
```

3. Install the package:
```bash
pip install -e .
```

## 📦 Dependencies

Key dependencies (see pyproject.toml for complete list):
- Flask 3.0.0
- Flask-CORS 4.0.0
- scikit-learn
- pandas
- numpy
- python-dateutil
- requests
- pyyaml
- typing-extensions
- psutil

## 🧪 Testing

Run tests with pytest:
```bash
pytest tests/
```

For coverage report:
```bash
pytest --cov=./ --cov-report=xml
```

## 🔒 Security

Security scanning is performed automatically on all commits using:
- Bandit for Python security scanning
- CodeQL for advanced security analysis
- GitHub Security features

## 🛠 Development

### Code Organization
- `zos_ml_demo/`: Main package directory
  - `utils/`: Utility modules
    - `zos_monitoring.py`: System monitoring utilities
    - `zos_performance_analyzer.py`: Performance analysis tools
    - `zos_security_manager.py`: Security management
    - Other utility modules...
  - `ml_model.py`: Machine learning models and algorithms

### CI/CD Pipeline
- Automated testing on Python 3.9-3.13
- Code coverage reporting
- Security scanning
- Linting with flake8

## 📊 Monitoring Features

The system monitoring module (`SystemMonitor`) provides:
- CPU usage tracking
- Memory utilization monitoring
- I/O metrics collection
- Response time analysis
- Transaction counting
- Error rate monitoring
- Health check reporting

## 🔍 Performance Analysis

The performance analyzer (`PerformanceAnalyzer`) includes:
- CPU analysis
- Memory analysis
- I/O analysis
- Response time analysis
- Automated recommendations
- Threshold-based alerts

## 📡 API Endpoints

### 1. Transaction Analysis
```bash
POST /api/analyze
Content-Type: application/json
X-User-ID: MLAPPADM

{
    "transaction": {
        "amount": 1000.00,
        "type": "TRANSFER",
        "source_account": "SAVINGS",
        "target_account": "CHECKING",
        "timestamp": "2025-02-28T12:00:00Z"
    }
}
```

### 2. Health Check
```bash
GET /api/health
X-User-ID: MLAPPADM
```

### 3. Performance Metrics
```bash
GET /api/performance
X-User-ID: MLAPPADM
```

### 4. Security Status
```bash
GET /api/security
X-User-ID: MLAPPADM
```

## 📝 Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔄 Version History

See [CHANGELOG.md](CHANGELOG.md) for version history and release notes.

## 🙏 Acknowledgments
- z/OS System Programming team
- ML Development team
- Security team
- Performance Engineering team
