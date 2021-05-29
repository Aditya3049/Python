# Time, Distance and Speed
# Tom is planning to design a Remote Controlled Mini Boat that is designed to travel across a still Lake

# Distance to Travel: 5 Km
# Speed of Boat: 10 km/hr

# Find the Arrival Time of the Boat in reaching its destination if the current time is provided.

# from datetime import datetime
# departure = datetime.now()
# Conversion Formula
# Time = Distance / Speed
from datetime import *
departure=datetime.now()
distance=5000
speed=10000
time1=distance/speed
arivaltime=departure + timedelta(hours=time1)
print(arivaltime)