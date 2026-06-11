import random
import pandas as pd
from datetime import datetime
import time
import os

csv_file = os.path.join("data", "sensor_logs.csv")

while True:

    temperature = random.randint(22, 40)
    humidity = random.randint(40, 90)
    soil = random.randint(0, 4095)
    water = random.randint(0, 4095)

    pump = "ON" if soil < 2000 else "OFF"

    data = {
        "Timestamp": datetime.now(),
        "Temperature": temperature,
        "Humidity": humidity,
        "Soil": soil,
        "Water": water,
        "Pump": pump
    }

    df = pd.DataFrame([data])

    try:
        old_df = pd.read_csv(csv_file)
        df = pd.concat([old_df, df], ignore_index=True)
    except:
        pass

    df.to_csv(csv_file, index=False)

    print("New Sensor Data Added")

    time.sleep(5)