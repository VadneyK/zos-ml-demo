# Installation Guide

## Prerequisites

### Python Version
This project requires Python 3.9 or higher due to dependencies on modern features in packages like pandas and scikit-learn.

### System Requirements
- Python >= 3.9
- pip (latest version)
- Virtual environment (recommended)
- z/OS system with required permissions

### z/OS Requirements
- z/OS 2.3 or higher
- RACF access
- DB2 permissions
- CICS regions access
- IMS configuration
- MQ setup

## Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/VadneyK/zos-ml-demo.git
cd zos-ml-demo
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Verify installation:
```bash
python -m pytest
```

## Configuration

### Environment Variables
Set the following environment variables:
```bash
export ZOS_CONFIG_PATH=/etc/zos/config
export LOG_LEVEL=INFO
export SSL_CERT_PATH=/etc/ssl/certs
export SSL_KEY_PATH=/etc/ssl/private
```

### z/OS Configuration
1. Set up RACF permissions
2. Configure DB2 connection
3. Set up CICS regions
4. Configure IMS access
5. Set up MQ channels

## Verification

Run the health check:
```bash
curl -H "X-User-ID: MLAPPADM" http://localhost:5002/api/health
```

Expected response:
```json
{
    "status": "healthy",
    "metrics": {
        "cpu": 19.75,
        "memory": 83.4,
        "io_wait": 0.0
    }
}
```

## Troubleshooting

### Common Issues

1. Python Version Error
```
Error: No matching distribution found for pandas>=2.2.0
```
Solution: Upgrade Python to version 3.9 or higher

2. Permission Issues
```
Error: RACF authentication failed
```
Solution: Verify RACF permissions and user ID

3. Connection Issues
```
Error: Unable to connect to DB2
```
Solution: Check DB2 configuration and credentials

## Next Steps

1. Review the [Quick Start](quickstart.md) guide
2. Configure [Security Settings](features/security.md)
3. Set up [Monitoring](features/performance-monitoring.md)
