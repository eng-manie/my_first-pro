import os
import datetime

log_file = "network_log.txt"
# سنقوم بعمل Ping لـ 5 حزم (packets) لضمان الدقة
target = "8.8.8.8"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# -c 5 تعني إرسال 5 حزم
response = os.system(f"ping -c 5 {target} > /dev/null")

if response == 0:
    status = "Connected"
else:
    status = "Disconnected"

with open(log_file, "a") as f:
    f.write(f"[{now}] Target: {target} | Status: {status}\n")

print(f"Check completed: {status}")


