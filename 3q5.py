from datetime import datetime

today = datetime.now()

print("Current Month Number:", today.month)
print("Current Month Name:", today.strftime("%B"))
