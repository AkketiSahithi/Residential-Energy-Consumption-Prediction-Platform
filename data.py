import pandas as pd
import numpy as np
from datetime import datetime, timedelta
start_time=datetime(2007, 1, 1, 0, 0)
timestamps=[start_time+timedelta(minutes=i) for i in range(1500)]
dates=[dt.strftime('%d-%m-%Y')for dt in timestamps]
times=[dt.strftime('%I:%M:%S %p')for dt in timestamps]
np.random.seed(42)
global_active_power=np.random.normal(loc=2.5, scale=0.1, size=1500).round(3)
global_reactive_power=np.random.normal(loc=0.1, scale=0.02, size=1500).round(3)
voltage=np.random.normal(loc=241.5, scale=0.5, size=1500).round(2)
global_intensity=(global_active_power*1000/voltage).round(1)
sub_metering_1=np.random.randint(0, 2, size=1500)
sub_metering_2=np.random.randint(0, 2, size=1500)
sub_metering_3=np.random.randint(0, 2, size=1500)
data={
    "Date": dates,
    "Time": times,
    "Global_active_power":global_active_power,
    "Global_reactive_power":global_reactive_power,
    "voltage":voltage,
    "Global_intensity":global_intensity,
    "sub_metering_1":sub_metering_1,
    "sub_metering_2":sub_metering_2,
    "sub_metering_3":sub_metering_3,
}
df=pd.DataFrame(data)
df.to_csv("energy_data.csv",index=False)
print("dataset as energy_data.csv")