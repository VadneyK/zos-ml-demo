"""
Advanced z/OS Performance Analysis
"""
import logging
from datetime import datetime, timedelta
import numpy as np

class PerformanceAnalyzer:
    def __init__(self):
        self.metrics = {}
        self.thresholds = {
            'cpu_usage': 80,
            'memory_usage': 85,
            'response_time': 2000,
            'io_wait': 5
        }

    def _analyze_response_times(self, response_times):
        if not response_times:
            return {'status': 'warning', 'message': 'No response time data available'}
        
        avg_response_time = sum(response_times) / len(response_times)
        if avg_response_time > self.thresholds['response_time']:
            return {
                'status': 'critical',
                'message': f'High average response time: {avg_response_time}ms'
            }
        return {'status': 'normal', 'message': 'Response times within acceptable range'}

    def analyze_performance(self, metrics_data):
        try:
            analysis = {
                'cpu': self._analyze_cpu(metrics_data.get('cpu_usage', [])),
                'memory': self._analyze_memory(metrics_data.get('memory_usage', [])),
                'response_times': self._analyze_response_times(metrics_data.get('response_times', [])),
                'io': self._analyze_io(metrics_data.get('io_wait', []))
            }
            return {
                'status': 'success',
                'analysis': analysis,
                'recommendations': self._generate_recommendations(analysis)
            }
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def _analyze_cpu(self, cpu_usage):
        if not cpu_usage:
            return {'status': 'warning', 'message': 'No CPU data available'}
        
        avg_cpu = sum(cpu_usage) / len(cpu_usage)
        if avg_cpu > self.thresholds['cpu_usage']:
            return {
                'status': 'critical',
                'message': f'High CPU usage: {avg_cpu}%'
            }
        return {'status': 'normal', 'message': 'CPU usage within acceptable range'}

    def _analyze_memory(self, memory_usage):
        if not memory_usage:
            return {'status': 'warning', 'message': 'No memory data available'}
        
        avg_memory = sum(memory_usage) / len(memory_usage)
        if avg_memory > self.thresholds['memory_usage']:
            return {
                'status': 'critical',
                'message': f'High memory usage: {avg_memory}%'
            }
        return {'status': 'normal', 'message': 'Memory usage within acceptable range'}

    def _analyze_io(self, io_wait):
        if not io_wait:
            return {'status': 'warning', 'message': 'No I/O data available'}
        
        avg_io = sum(io_wait) / len(io_wait)
        if avg_io > self.thresholds['io_wait']:
            return {
                'status': 'critical',
                'message': f'High I/O wait time: {avg_io}s'
            }
        return {'status': 'normal', 'message': 'I/O wait times within acceptable range'}

    def _generate_recommendations(self, analysis):
        recommendations = []
        
        if analysis['cpu']['status'] == 'critical':
            recommendations.append({
                'component': 'CPU',
                'action': 'Consider scaling CPU resources or optimizing CPU-intensive operations'
            })
            
        if analysis['memory']['status'] == 'critical':
            recommendations.append({
                'component': 'Memory',
                'action': 'Increase memory allocation or investigate memory leaks'
            })
            
        if analysis['response_times']['status'] == 'critical':
            recommendations.append({
                'component': 'Response Time',
                'action': 'Optimize database queries and application code'
            })
            
        if analysis['io']['status'] == 'critical':
            recommendations.append({
                'component': 'I/O',
                'action': 'Optimize I/O operations or consider faster storage'
            })
            
        return recommendations
