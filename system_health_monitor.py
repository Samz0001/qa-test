import psutil
import logging

logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def check_cpu_usage():
    usage = psutil.cpu_percent(interval=1)
    if usage > 80:
        logging.warning(f"High CPU usage detected: {usage}%")
    return usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    if memory.percent > 80:
        logging.warning(f"High memory usage detected: {memory.percent}%")
    return memory.percent

if __name__ == "__main__":
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
