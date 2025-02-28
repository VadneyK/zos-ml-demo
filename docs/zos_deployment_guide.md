# z/OS Deployment Guide

## Table of Contents
1. [Container-based Deployment (zCX)](#container-based-deployment)
2. [Native z/OS Deployment](#native-zos-deployment)
3. [Security Configuration](#security-configuration)
4. [Monitoring and Management](#monitoring-and-management)

## Container-based Deployment

### Prerequisites
- z/OS V2R4 or later
- z/OS Container Extensions (zCX) installed
- Docker skills and knowledge
- Network access to required repositories

### Steps

1. **Prepare zCX Environment**
   ```bash
   # Verify zCX is running
   F IZUSVR1,DISPLAY
   ```

2. **Build Docker Image**
   ```dockerfile
   # Sample Dockerfile for z/OS
   FROM s390x/python:3.8
   WORKDIR /app
   COPY . .
   RUN pip install --no-cache-dir -r requirements.txt
   EXPOSE 5000
   CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
   ```

3. **Deploy Container**
   ```bash
   # Build image
   docker build -t zos-ml-demo .
   
   # Run container
   docker run -d -p 5000:5000 --name zos-ml-demo zos-ml-demo
   ```

## Native z/OS Deployment

### Prerequisites
- IBM Open Enterprise Python for z/OS
- USS (UNIX System Services) access
- OMVS segment defined
- Required APF authorizations

### Steps

1. **Set up USS Environment**
   ```bash
   # Create application directory
   mkdir -p /u/users/mlapp
   chmod 750 /u/users/mlapp
   ```

2. **Install Dependencies**
   ```bash
   # Set Python environment
   export PATH=/usr/lpp/IBM/python3.8/bin:$PATH
   export PYTHONPATH=/usr/lpp/IBM/python3.8/lib
   
   # Install packages
   pip install --no-cache-dir -r requirements.txt
   ```

3. **Configure Started Task**
   ```jcl
   //MLAPP    PROC
   //MLAPP    EXEC PGM=BPXBATCH,
   //         PARM='SH python /u/users/mlapp/app.py'
   //STDOUT   DD SYSOUT=*
   //STDERR   DD SYSOUT=*
   ```

## Security Configuration

### RACF Configuration
```racf
# Create RACF Group
ADDGROUP MLAPPGRP OMVS(GID(7xx))

# Create RACF User
ADDUSER MLAPPUSR DFLTGRP(MLAPPGRP) OMVS(UID(7xx))

# Grant Access
PERMIT MLAPP CLASS(STARTED) ID(MLAPPUSR) ACCESS(READ)
SETROPTS RACLIST(STARTED) REFRESH
```

### SSL/TLS Configuration
```bash
# Generate Certificate
RACDCERT GENCERT SITE SUBJECTSDN(CN='ML App') WITHLABEL('MLAPP')

# Connect Certificate
RACDCERT ADD('hlq.CERT.MLAPP') TRUST WITHLABEL('MLAPP')
```

## Monitoring and Management

### SMF Records
```jcl
//SMFCONF  EXEC PGM=IXCMIAPU
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
  DEFAULTLSNAME(IFASMF.LSNAME)
    DEFINE LOGSTREAM NAME(IFASMF.MLAPP)
    STRUCTNAME(IFASMF_GENERAL)
/*
```

### Healthcheck Configuration
```rexx
/* MLAPP Healthcheck */
check_name = 'MLAPP_CHECK'
check_owner = 'MLAPP'
```

### Automation
```automation
/* Automatic Recovery */
IF STATE(MLAPP) = DOWN THEN
  'S MLAPP'
```
