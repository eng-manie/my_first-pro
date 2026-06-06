import os
import datetime

# اسم ملف السجل
log_file = "network_log.txt"

# الحصول على الوقت الحالي
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# اختبار الاتصال
response = os.system("ping -c 1 8.8.8.8 > /dev/null")

if response == 0:
    status = "Connected"
else:
    status = "Disconnected"

# كتابة النتيجة في ملف السجل
with open(log_file, "a") as f:
    f.write(f"[{now}] Status: {status}\n")

print(f"Check completed: {status} at {now}")


