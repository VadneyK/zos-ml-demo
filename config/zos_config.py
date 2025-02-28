"""
z/OS specific configuration settings
"""
import os

# z/OS Environment Settings
ZOS_ENCODING = 'IBM-1047'  # EBCDIC encoding for z/OS
USS_ENCODING = 'ISO8859-1'  # USS file system encoding

# Security Settings
RACF_ENABLED = True
SSL_ENABLED = True
SSL_CERT_LABEL = 'MLAPP'
SSL_KEYRING = 'MLAPPRING'

# SMF Recording Settings
SMF_ENABLED = True
SMF_RECORD_TYPE = 230  # Custom SMF record type
SMF_RECORD_SUBTYPE = 1

# Logging Configuration
LOG_TO_OPERLOG = True
SYSLOG_FACILITY = 'LOCAL4'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# z/OS Resource Settings
MAX_CPU_TIME = 300  # seconds
MAX_MEMORY = '2G'
TEMP_SPACE = '/tmp'

# z/OS Dataset Configuration
DATASET_HLQ = 'MLAPP'
MODEL_DATASET = f"{DATASET_HLQ}.MODELS"
DATA_DATASET = f"{DATASET_HLQ}.DATA"

def get_zos_config():
    """Return z/OS specific configuration"""
    return {
        'encoding': ZOS_ENCODING,
        'uss_encoding': USS_ENCODING,
        'racf_enabled': RACF_ENABLED,
        'ssl_enabled': SSL_ENABLED,
        'ssl_cert_label': SSL_CERT_LABEL,
        'ssl_keyring': SSL_KEYRING,
        'smf_enabled': SMF_ENABLED,
        'smf_record_type': SMF_RECORD_TYPE,
        'smf_record_subtype': SMF_RECORD_SUBTYPE,
        'log_to_operlog': LOG_TO_OPERLOG,
        'syslog_facility': SYSLOG_FACILITY,
        'log_format': LOG_FORMAT,
        'max_cpu_time': MAX_CPU_TIME,
        'max_memory': MAX_MEMORY,
        'temp_space': TEMP_SPACE,
        'dataset_hlq': DATASET_HLQ,
        'model_dataset': MODEL_DATASET,
        'data_dataset': DATA_DATASET
    }
