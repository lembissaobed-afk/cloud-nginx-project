import psutil
import time

def monitor():
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log = f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"

    print(log)

    with open("monitor.log", "a") as f:
        f.write(log + "\n")

if __name__ == "__main__":
    while True:
        monitor()
        time.sleep(5)