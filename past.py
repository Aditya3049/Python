# Past and Present
# Below, the Current Date and Time has been stored in a variable.

# from datetime import datetime
# today = datetime.now()
# Find the Date exactly before 100 days and after 200 days.

# The Final Result should only display the Date and not the Time
from datetime import *
today=datetime.now()
past=today - timedelta(days=100)
Future=today + timedelta(days=200)
print(past)
print(Future)