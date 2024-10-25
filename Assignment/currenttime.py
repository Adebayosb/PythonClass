from datetime import datetime
currenttime = datetime.now()
formattedtime = currenttime.strftime("%H:%M:%S")
print(f"current system time: {formattedtime}")