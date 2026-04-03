#!/var/ossec/framework/python/bin/python3

import sys
import json
import requests
import uuid

# Configuration
THIVE_URL = "http://192.168.0.100:9000/thehive/api/alert"
API_KEY = "ymElbfkyW+MdCrKGt+cSvSQd4W3U1wkY"

def main():
    if len(sys.argv) < 2:
        return

    alert_file = sys.argv[1]
    
    try:
        with open(alert_file, 'r') as f:
            alert_json = json.load(f)
        
        # Prepare the payload for TheHive
        payload = {
            "title": f"Wazuh Alert: {alert_json.get('rule', {}).get('description', 'Unknown')}",
            "description": (
                f"Rule ID: {alert_json['rule']['id']}\n"
                f"Level: {alert_json['rule']['level']}\n"
                f"Agent: {alert_json.get('agent', {}).get('name', 'N/A')}\n"
                f"Log: {alert_json.get('full_log', '')}"
            ),
            "severity": 2,
            "source": "wazuh",
            "type": "wazuh_alert",
            "sourceRef": str(uuid.uuid4())[:6],
            "tags": ["wazuh", alert_json.get('agent', {}).get('name', 'no-agent')]
        }

        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }

        # Send the request
        r = requests.post(THIVE_URL, data=json.dumps(payload), headers=headers)
        print(f"Status: {r.status_code}, Response: {r.text}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
