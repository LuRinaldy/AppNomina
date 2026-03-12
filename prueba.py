from datetime import datetime, timedelta

hoy = datetime(2026, 1, 10, 22, 0)
mañana = hoy + timedelta(days=1)
print(mañana)