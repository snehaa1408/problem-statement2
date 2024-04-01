import psutil

# Define thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    if cpu_percent > CPU_THRESHOLD:
        print(f"High CPU usage detected: {cpu_percent}%")

def check_memory_usage():
    memory_percent = psutil.virtual_memory().percent
    if memory_percent > MEMORY_THRESHOLD:
        print(f"High memory usage detected: {memory_percent}%")

def check_disk_usage():
    partitions = psutil.disk_partitions()
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        if usage.percent > DISK_THRESHOLD:
            print(f"High disk usage detected on {partition.mountpoint}: {usage.percent}%")

def check_running_processes():
    processes = psutil.process_iter()
    for process in processes:
        try:
            process_info = process.as_dict(attrs=['name', 'cpu_percent', 'memory_percent'])
            if process_info['cpu_percent'] > CPU_THRESHOLD or process_info['memory_percent'] > MEMORY_THRESHOLD:
                print(f"High resource usage detected for process {process_info['name']}: CPU {process_info['cpu_percent']}%, Memory {process_info['memory_percent']}%")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
def main():
    print("Monitoring system health...")
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        check_running_processes()

if __name__ == "__main__":
    main()
