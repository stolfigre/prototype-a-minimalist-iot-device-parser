Python
# 72q2_prototype_a_min.py
# Minimalist IoT device parser prototype

import json
import requests

# Configuration
DEVICE_API_URL = "https://api.example.com/devices"
PARSE_DEVICE_DATA = True

# Device data structure
device_data = {
    "device_id": "",
    "device_type": "",
    "temperature": 0.0,
    "humidity": 0.0,
    "timestamp": 0
}

def fetch_device_data(device_id):
    response = requests.get(f"{DEVICE_API_URL}/{device_id}")
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        return None

def parse_device_data(raw_data):
    device_data["device_id"] = raw_data["id"]
    device_data["device_type"] = raw_data["type"]
    device_data["temperature"] = raw_data["data"]["temperature"]
    device_data["humidity"] = raw_data["data"]["humidity"]
    device_data["timestamp"] = raw_data["data"]["timestamp"]
    return device_data

def main():
    device_id = "device-123"  # Replace with actual device ID
    raw_data = fetch_device_data(device_id)
    if raw_data:
        if PARSE_DEVICE_DATA:
            parsed_data = parse_device_data(raw_data)
            print("Parsed device data:")
            print(json.dumps(parsed_data, indent=4))
        else:
            print("Raw device data:")
            print(json.dumps(raw_data, indent=4))
    else:
        print("Failed to fetch device data")

if __name__ == "__main__":
    main()