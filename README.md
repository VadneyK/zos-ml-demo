# z/OS Machine Learning Transaction Analyzer

A comprehensive machine learning application designed for z/OS environments, focusing on transaction pattern analysis, anomaly detection, and system monitoring.

## 🌟 Features

### 1. Transaction Analysis
- Real-time transaction pattern detection
- Risk scoring and anomaly detection
- Integration with z/OS subsystems (DB2, IMS, CICS, MQ)
- VSAM quick lookup storage

### 2. Performance Management
- Real-time system metrics monitoring
- RMF/SMF metric collection
- Performance trend analysis
- Resource utilization tracking
- Automated recommendations

### 3. Security Features
- RACF permission verification
- Comprehensive security auditing
- Suspicious pattern detection
- Security event logging
- Detailed security reporting

### 4. System Integration
- DB2 transaction storage
- IMS transaction processing
- CICS transaction handling
- MQ asynchronous processing
- System Automation
- Parallel Sysplex support

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- z/OS environment
- Required Python packages (see requirements.txt)

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd zos-ml-demo
```

2. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Start the application:
```bash
python app.py
```

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

## 📊 Monitoring and Metrics

### System Metrics
- CPU utilization
- Memory usage
- I/O performance
- Response times
- Transaction rates

### Performance Analysis
- Real-time performance monitoring
- Trend analysis
- Automated recommendations
- Resource optimization suggestions

### Security Monitoring
- Access pattern analysis
- Security event tracking
- Suspicious activity detection
- RACF integration

## 🔒 Security

### Authentication
- RACF-based authentication
- Role-based access control
- Comprehensive audit trails

### Data Protection
- SSL/TLS encryption
- Secure data storage
- Access logging

## 🛠 Configuration

### Environment Variables
- `ZOS_CONFIG_PATH`: Path to z/OS configuration file
- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR)
- `SSL_CERT_PATH`: Path to SSL certificate
- `SSL_KEY_PATH`: Path to SSL private key

### z/OS Configuration
- DB2 connection settings
- IMS configuration
- CICS settings
- MQ configuration
- RACF settings

## 📝 Logging

### System Logs
- Application logs
- Performance metrics
- Security events
- Transaction records

### Monitoring Data
- RMF records
- SMF data
- WLM metrics
- Sysplex status

## 🔧 Maintenance

### Backup
- Regular transaction backups
- Configuration backups
- Security audit trails

### Recovery
- Transaction recovery procedures
- System state recovery
- Error handling protocols

## 📈 Performance Optimization

### Recommendations
- Resource allocation optimization
- Workload balancing
- Response time improvement
- I/O optimization

## 🤝 Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments
- z/OS System Programming team
- ML Development team
- Security team
- Performance Engineering team
