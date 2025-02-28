import pytest
from utils.zos_performance_analyzer import PerformanceAnalyzer
from utils.zos_monitoring import SystemMonitor

@pytest.fixture
def performance_analyzer():
    return PerformanceAnalyzer()

@pytest.fixture
def system_monitor():
    return SystemMonitor()

def test_cpu_analysis(performance_analyzer):
    metrics = {
        'cpu_usage': 75.0,
        'process_count': 100,
        'thread_count': 500
    }
    analysis = performance_analyzer.analyze_cpu(metrics)
    assert isinstance(analysis, dict)
    assert 'status' in analysis
    assert 'message' in analysis

def test_memory_analysis(performance_analyzer):
    metrics = {
        'memory_usage': 80.0,
        'available_memory': 8192,
        'total_memory': 16384
    }
    analysis = performance_analyzer.analyze_memory(metrics)
    assert isinstance(analysis, dict)
    assert 'status' in analysis
    assert 'message' in analysis

def test_io_analysis(performance_analyzer):
    metrics = {
        'io_wait': 5.0,
        'disk_usage': 65.0,
        'iops': 1000
    }
    analysis = performance_analyzer.analyze_io(metrics)
    assert isinstance(analysis, dict)
    assert 'status' in analysis
    assert 'message' in analysis

def test_system_monitoring(system_monitor):
    metrics = system_monitor.get_system_metrics()
    assert isinstance(metrics, dict)
    assert 'cpu' in metrics
    assert 'memory' in metrics
    assert 'io_wait' in metrics
