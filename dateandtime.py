from datetime import *
today=datetime.now()
print(today)
print(today.date())
print(today.time())
a=today + timedelta(days=365)
print(a)
b=today - timedelta(days=365)
print(b)