### ​Project Overview

​This project provides a comprehensive implementation for a modern Security Operations Center (SOC). It establishes a streamlined pipeline where firewall logs from OPNsense are ingested and analyzed by Wazuh. Upon detecting a high-severity event, an alert is automatically forwarded to TheHive to initiate the incident response lifecycle. The model is specifically optimized for isolated (Air-gapped) environments.

### ​Repository Files and Description

- ​**custom-w2thive.py**: The main Python integration script that handles the logic for forwarding alerts to TheHive API.
- ​**thehive4py**: A Bash wrapper script used to execute the Python integration within the Wazuh framework environment.
- ​**opnsense-decoder.xml**: A custom XML decoder designed to parse and structure raw OPNsense firewall logs within Wazuh.
- ​**opnsense-rules.xml**: Security rules tailored to identify threats and anomalies specifically within OPNsense traffic.
- ​**images./**: A dedicated folder containing architectural diagrams, dashboard screenshots, and implementation results.

### ​Minimum System Requirements

​To successfully deploy and run this SOC framework, the following hardware resources are required at a minimum:

- ​**Wazuh Manager**: Minimum 4GB RAM.
- ​**TheHive Platform**: Minimum 5GB RAM.
- ​**OPNsense Firewall**: Minimum 2GB RAM.

​**Prepared by:** Ibrahim Al-Shahari

د
