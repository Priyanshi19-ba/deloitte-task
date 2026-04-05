from datetime import datetime

def convert_to_millis(iso_time):
    dt = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%SZ")
    return int(dt.timestamp() * 1000)

def convertFromFormat1(jsonObject):
    return {
        "deviceId": jsonObject["deviceId"],
        "timestamp": convert_to_millis(jsonObject["timestamp"]),
        "temperature": jsonObject["temp"],
        "humidity": jsonObject["humidity"]
    }

def convertFromFormat2(jsonObject):
    return {
        "deviceId": jsonObject["id"],
        "timestamp": convert_to_millis(jsonObject["time"]),
        "temperature": jsonObject["temperature"],
        "humidity": jsonObject["hum"]
    }
