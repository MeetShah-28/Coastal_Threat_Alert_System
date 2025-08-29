# backend.py
import random
import time

# Function to simulate sensor data
def generate_data():
    return {
        "tide": random.uniform(1, 8),  # meters
        "wind": random.uniform(10, 150),  # km/h
        "pollution": random.uniform(50, 300)  # AQI
    }

# Function to check for anomalies
def check_alert(data):
    alerts = []
    if data["tide"] > 5:
        alerts.append("🌊 Flood Risk: Tide above 5m")
    if data["wind"] > 100:
        alerts.append("🌪️ Cyclone Risk: Wind speed above 100 km/h")
    if data["pollution"] > 200:
        alerts.append("☣️ Pollution Risk: AQI above 200")
    return alerts if alerts else ["✅ All Safe"]

# Test run
if __name__ == "__main__":
    for _ in range(5):
        d = generate_data()
        print(d, check_alert(d))
        time.sleep(1)
