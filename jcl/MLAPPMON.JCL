//MLAPPMON JOB (ACCT),'ML APP MONITOR',
//             CLASS=A,MSGCLASS=X,MSGLEVEL=(1,1)
//*
//********************************************************************
//* Advanced Monitoring and Security Setup for ML Application
//********************************************************************
//MONITOR  EXEC PGM=MLMONITOR
//STEPLIB  DD   DSN=MLAPP.LOADLIB,DISP=SHR
//SYSPRINT DD   SYSOUT=*
//SYSIN    DD   *
  MONITOR_INTERVAL=300
  PERF_THRESHOLD=85
  LOG_LEVEL=INFO
  SECURITY_AUDIT=YES
  RMF_COLLECT=YES
  SMF_RECORDS=YES
/*
//SECAUDIT EXEC PGM=MLSECAUD
//STEPLIB  DD   DSN=MLAPP.LOADLIB,DISP=SHR
//SYSPRINT DD   SYSOUT=*
//AUDITLOG DD   DSN=MLAPP.AUDIT.LOG,DISP=MOD
//SYSIN    DD   *
  AUDIT_LEVEL=HIGH
  RACF_CHECK=YES
  PATTERN_DETECT=YES
/*
