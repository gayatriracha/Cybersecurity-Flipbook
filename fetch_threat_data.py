# Script to fetch latest cybersecurity threat data
import requests

def fetch_threat_data():
    url = "https://cve.circl.lu/api/last"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return []

if __name__ == "__main__":
    data = fetch_threat_data()
    print("Fetched", len(data), "threat reports")