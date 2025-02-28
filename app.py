from flask import Flask, request, jsonify
from flask_cors import CORS
from ml_model import TransactionAnalyzer
import numpy as np
import time
from config.zos_config import get_zos_config
from utils.zos_integration import ZOSIntegration
from utils.zos_monitoring import ZOSMonitor
from utils.zos_resource_manager import ZOSResourceManager
from utils.zos_extended_monitoring import ZOSExtendedMonitor
from utils.zos_subsystem_integration import (
    ZOSDB2Integration,
    ZOSIMSIntegration,
    ZOSCICSIntegration,
    ZOSMQIntegration,
    ZOSVSAMIntegration
)
from utils.zos_advanced_subsystems import (
    ZOSSystemAutomation,
    ZOSParallelSysplex,
    ZOSWorkloadScheduler,
    ZOSDatasetServices,
    ZOSSecurityServer,
    ZOSNetworkServices
)
from utils.zos_performance_analyzer import ZOSPerformanceAnalyzer
from utils.zos_security_manager import ZOSSecurityManager
import logging
from datetime import datetime
import uuid
import random

app = Flask(__name__)
CORS(app)

# Initialize z/OS components
zos_config = get_zos_config()
zos = ZOSIntegration(zos_config)
monitor = ZOSMonitor(zos_config)
ext_monitor = ZOSExtendedMonitor(zos_config)
perf_analyzer = ZOSPerformanceAnalyzer()
security_manager = ZOSSecurityManager(zos_config)
resource_manager = ZOSResourceManager(zos_config)

# Initialize advanced subsystems
automation = ZOSSystemAutomation(zos_config)
sysplex = ZOSParallelSysplex(zos_config)
scheduler = ZOSWorkloadScheduler(zos_config)
dataset_svc = ZOSDatasetServices(zos_config)
security_svc = ZOSSecurityServer(zos_config)
network_svc = ZOSNetworkServices(zos_config)

# Initialize subsystem integrations
db2 = ZOSDB2Integration(zos_config)
ims = ZOSIMSIntegration(zos_config)
cics = ZOSCICSIntegration(zos_config)
mq = ZOSMQIntegration(zos_config)
vsam = ZOSVSAMIntegration(zos_config)

# Initialize model
model = TransactionAnalyzer()

@app.route('/api/health', methods=['GET'])
def health_check():
    try:
        # Get system metrics
        metrics = {
            'cpu_usage': monitor.get_cpu_metrics(),
            'memory_usage': monitor.get_memory_metrics(),
            'io_wait': monitor.get_io_metrics(),
            'response_times': monitor.get_response_times()
        }
        
        # Analyze performance
        perf_status = perf_analyzer.analyze_performance(metrics)
        
        # Basic health status
        health_status = {
            'status': 'healthy',
            'timestamp': datetime.now().isoformat(),
            'metrics': {
                'cpu': sum(metrics['cpu_usage']) / len(metrics['cpu_usage']) if metrics['cpu_usage'] else 0,
                'memory': sum(metrics['memory_usage']) / len(metrics['memory_usage']) if metrics['memory_usage'] else 0,
                'io_wait': sum(metrics['io_wait']) / len(metrics['io_wait']) if metrics['io_wait'] else 0,
                'avg_response_time': sum(metrics['response_times']) / len(metrics['response_times']) if metrics['response_times'] else 0
            },
            'performance_analysis': perf_status,
            'recommendations': perf_status.get('recommendations', [])
        }
        
        return jsonify(health_status)
    except Exception as e:
        app.logger.error(f"Health check failed: {str(e)}")
        return jsonify({
            'status': 'error',
            'error': str(e)
        }), 500

@app.route('/api/analyze', methods=['POST'])
def analyze_transaction():
    """Analyze a transaction for patterns and anomalies"""
    start_time = time.time()
    success = False
    
    try:
        # Enhanced security check
        user_id = request.headers.get('X-User-ID', 'UNKNOWN')
        if not security_manager.verify_racf_permissions(user_id, 'MLAPP.ANALYZE', 'READ'):
            return jsonify({'error': 'Unauthorized'}), 403

        data = request.json
        if not data or 'transaction' not in data:
            return jsonify({'error': 'Invalid request data'}), 400

        transaction = data['transaction']
        required_fields = ['amount', 'type', 'source_account', 'target_account', 'timestamp']
        for field in required_fields:
            if field not in transaction:
                return jsonify({'error': f'Missing required field: {field}'}), 400

        # Analyze transaction
        analysis_result = {
            'transaction_id': str(uuid.uuid4()),
            'timestamp': datetime.now().isoformat(),
            'analysis': {
                'risk_score': random.uniform(0, 1),  # Simulated risk score
                'patterns': [
                    'NORMAL_TRANSFER_PATTERN',
                    'EXPECTED_AMOUNT_RANGE'
                ],
                'anomalies': []
            },
            'recommendations': []
        }

        # Add recommendations based on analysis
        if analysis_result['analysis']['risk_score'] > 0.7:
            analysis_result['recommendations'].append({
                'type': 'HIGH_RISK',
                'message': 'Transaction shows high-risk patterns'
            })

        success = True
        return jsonify(analysis_result)

    except Exception as e:
        app.logger.error(f"Transaction analysis failed: {str(e)}")
        return jsonify({'error': str(e)}), 500
        
    finally:
        end_time = time.time()
        monitor.record_transaction(start_time, end_time, success)

@app.route('/api/performance', methods=['GET'])
def get_performance():
    """Get performance metrics and analysis"""
    try:
        if not security_manager.verify_racf_permissions(
            request.headers.get('X-User-ID', 'UNKNOWN'),
            'MLAPP.PERFORMANCE',
            'READ'
        ):
            return jsonify({'error': 'Unauthorized'}), 403

        # Get current metrics
        metrics = {
            'cpu_usage': monitor.get_cpu_metrics(),
            'memory_usage': monitor.get_memory_metrics(),
            'io_wait': monitor.get_io_metrics(),
            'response_times': monitor.get_response_times()
        }
        
        # Analyze performance
        analysis = perf_analyzer.analyze_performance(metrics)
        
        return jsonify({
            'status': 'success',
            'timestamp': datetime.now().isoformat(),
            'metrics': metrics,
            'analysis': analysis
        })
    except Exception as e:
        app.logger.error(f"Performance report generation failed: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/security', methods=['GET'])
def get_security():
    """Get comprehensive security report"""
    try:
        if not security_manager.verify_racf_permissions(
            request.headers.get('X-User-ID', 'UNKNOWN'),
            'MLAPP.SECURITY',
            'READ'
        ):
            return jsonify({'error': 'Unauthorized'}), 403
            
        return jsonify(security_manager.generate_security_report())
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    # Setup recovery environment
    if not resource_manager.setup_recovery_environment():
        raise RuntimeError("Failed to setup recovery environment")
        
    # Initialize automation
    automation.define_resource('MLAPP', 'APPLICATION')
    
    # Join sysplex
    sysplex.join_sysplex('PRODPLEX')
    
    # Schedule monitoring jobs
    scheduler.schedule_job('MLAPPMON', '*/15 * * * *')  # Every 15 minutes
    
    # Configure network
    network_svc.start_tcp_listener(5000, 'MLAPP')
    
    # Start monitoring threads
    import threading
    logger = logging.getLogger(__name__)

    def monitoring_thread():
        while True:
            monitor.check_thresholds()
            ext_monitor.write_rmf_monitor_i_data(
                ext_monitor.collect_system_metrics()
            )
            time.sleep(60)  # Check every minute
            
    def subsystem_monitor_thread():
        while True:
            # Collect and write subsystem metrics
            db2_metrics = ext_monitor.collect_db2_metrics()
            ims_metrics = ext_monitor.collect_ims_metrics()
            cics_metrics = ext_monitor.collect_cics_metrics()
            
            ext_monitor.write_smf_extended_records({
                'db2': db2_metrics,
                'ims': ims_metrics,
                'cics': cics_metrics
            }, record_type=231)
            
            time.sleep(300)  # Check every 5 minutes
            
    def performance_analyzer_thread():
        while True:
            metrics_data = {
                'cpu_usage': monitor.get_cpu_metrics(),
                'memory_usage': monitor.get_memory_metrics(),
                'response_times': monitor.get_response_times(),
                'io_wait': monitor.get_io_metrics()
            }
            analysis = perf_analyzer.analyze_performance(metrics_data)
            if analysis['status'] == 'critical':
                for rec in analysis['recommendations']:
                    logger.warning(f"Performance Alert: {rec['component']} - {rec['action']}")
            time.sleep(60)  # Check every minute
            
    def security_monitor_thread():
        while True:
            security_analysis = security_manager.monitor_security_events()
            if security_analysis and security_analysis['suspicious_patterns']:
                for pattern in security_analysis['suspicious_patterns']:
                    security_manager.audit_transaction({
                        'type': 'SECURITY_ALERT',
                        'pattern': pattern,
                        'timestamp': time.time()
                    })
            time.sleep(60)  # Check every minute
    
    threading.Thread(target=monitoring_thread, daemon=True).start()
    threading.Thread(target=subsystem_monitor_thread, daemon=True).start()
    threading.Thread(target=performance_analyzer_thread, daemon=True).start()
    threading.Thread(target=security_monitor_thread, daemon=True).start()
    
    # Run the application
    app.run(host='0.0.0.0', port=5002, debug=True)
