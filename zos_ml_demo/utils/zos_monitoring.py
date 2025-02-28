"""
z/OS Monitoring Utilities
"""
import os
import time
import json
import logging
import psutil
from datetime import datetime

class ZOSMonitor:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger('zos_monitor')
        self.metrics = {
            'cpu': [],
            'memory': [],
            'io': [],
            'response_times': [],
            'transactions': 0,
            'errors': 0
        }
        self.thresholds = {
            'cpu': 80,
            'memory': 85,
            'io': 70,
            'response_time': 2000,
            'response_time_threshold': 1.0,
            'error_rate_threshold': 0.1
        }

    def get_cpu_metrics(self):
        """Get CPU usage metrics"""
        try:
            cpu_percent = psutil.cpu_percent(interval=1)
            self.metrics['cpu'].append(cpu_percent)
            if len(self.metrics['cpu']) > 60:  # Keep last hour of data
                self.metrics['cpu'].pop(0)
            return self.metrics['cpu']
        except Exception as e:
            self.logger.error(f"Error getting CPU metrics: {e}")
            return []

    def get_memory_metrics(self):
        """Get memory usage metrics"""
        try:
            memory = psutil.virtual_memory()
            memory_percent = memory.percent
            self.metrics['memory'].append(memory_percent)
            if len(self.metrics['memory']) > 60:
                self.metrics['memory'].pop(0)
            return self.metrics['memory']
        except Exception as e:
            self.logger.error(f"Error getting memory metrics: {e}")
            return []

    def get_io_metrics(self):
        """Get I/O metrics"""
        try:
            io = psutil.disk_io_counters()
            io_wait = psutil.cpu_times().iowait if hasattr(psutil.cpu_times(), 'iowait') else 0
            self.metrics['io'].append(io_wait)
            if len(self.metrics['io']) > 60:
                self.metrics['io'].pop(0)
            return self.metrics['io']
        except Exception as e:
            self.logger.error(f"Error getting I/O metrics: {e}")
            return []

    def get_response_times(self):
        """Get response time metrics"""
        try:
            # Simulate response times for demo
            response_time = self.metrics['response_times'][-1] if self.metrics['response_times'] else 100
            response_time = max(50, min(500, response_time + ((-50 + time.time() % 100) / 2)))
            self.metrics['response_times'].append(response_time)
            if len(self.metrics['response_times']) > 60:
                self.metrics['response_times'].pop(0)
            return self.metrics['response_times']
        except Exception as e:
            self.logger.error(f"Error getting response times: {e}")
            return []

    def write_wto_message(self, message):
        """Write to Operator message"""
        # In production, this would use proper WTO facility
        self.logger.info(f"WTO: {message}")

    def write_health_check(self):
        """Write Health Check data"""
        health_data = {
            'timestamp': datetime.now().isoformat(),
            'transactions_total': self.metrics['transactions'],
            'errors_total': self.metrics['errors'],
            'avg_response_time': sum(self.metrics['response_times']) / len(self.metrics['response_times']) 
                if self.metrics['response_times'] else 0,
            'cpu_usage': sum(self.metrics['cpu']) / len(self.metrics['cpu'])
                if self.metrics['cpu'] else 0,
            'memory_usage': sum(self.metrics['memory']) / len(self.metrics['memory'])
                if self.metrics['memory'] else 0
        }
        
        # Write to SMF record
        self._write_smf_health_record(health_data)
        
        # Write to z/OS dataset
        self._write_health_dataset(health_data)

    def _write_smf_health_record(self, health_data):
        """Write health data to SMF"""
        try:
            # Format for SMF record type 230 subtype 2 (Health)
            record = {
                'timestamp': health_data['timestamp'],
                'record_type': 230,
                'subtype': 2,
                'data': health_data
            }
            self.logger.info(f"Writing health SMF record: {record}")
        except Exception as e:
            self.logger.error(f"Failed to write health SMF record: {str(e)}")

    def _write_health_dataset(self, health_data):
        """Write health data to z/OS dataset"""
        try:
            dataset_name = f"{self.config['dataset_hlq']}.HEALTH"
            self.logger.info(f"Writing health data to dataset: {dataset_name}")
        except Exception as e:
            self.logger.error(f"Failed to write health dataset: {str(e)}")

    def check_thresholds(self):
        """Check if any metrics exceed thresholds"""
        alerts = []
        
        # Check CPU
        if self.metrics['cpu'] and self.metrics['cpu'][-1] > self.thresholds['cpu']:
            alerts.append({
                'component': 'CPU',
                'value': self.metrics['cpu'][-1],
                'threshold': self.thresholds['cpu']
            })
            
        # Check Memory
        if self.metrics['memory'] and self.metrics['memory'][-1] > self.thresholds['memory']:
            alerts.append({
                'component': 'Memory',
                'value': self.metrics['memory'][-1],
                'threshold': self.thresholds['memory']
            })
            
        # Check I/O
        if self.metrics['io'] and self.metrics['io'][-1] > self.thresholds['io']:
            alerts.append({
                'component': 'I/O',
                'value': self.metrics['io'][-1],
                'threshold': self.thresholds['io']
            })
            
        # Check Response Time
        avg_response_time = (sum(self.metrics['response_times']) / 
            len(self.metrics['response_times'])) if self.metrics['response_times'] else 0
        
        if avg_response_time > self.thresholds['response_time_threshold']:
            self.write_wto_message(
                f"WARNING: Average response time ({avg_response_time:.2f}s) "
                f"exceeds threshold"
            )
        
        # Check Error Rate
        error_rate = (self.metrics['errors'] / self.metrics['transactions'] 
            if self.metrics['transactions'] > 0 else 0)
        
        if error_rate > self.thresholds['error_rate_threshold']:
            self.write_wto_message(
                f"WARNING: Error rate ({error_rate:.2%}) exceeds threshold"
            )
            
        return alerts

    def record_transaction(self, start_time, end_time, success):
        """Record transaction timing"""
        try:
            response_time = (end_time - start_time) * 1000  # Convert to ms
            self.metrics['response_times'].append(response_time)
            if len(self.metrics['response_times']) > 60:
                self.metrics['response_times'].pop(0)
                
            self.metrics['transactions'] += 1
            if not success:
                self.metrics['errors'] += 1
                
            if response_time > self.thresholds['response_time']:
                self.write_wto_message(f"Warning: High response time detected: {response_time}ms")
        except Exception as e:
            self.logger.error(f"Error recording transaction: {e}")
