import psutil
import time
import os

def cpu_mem_stress(cpu_percent, mem_percent, duration):
    # Calculate the amount of CPU and memory to allocate
    cpu_count = os.cpu_count()
    cpu_load = cpu_percent * cpu_count / 100
    mem_load = psutil.virtual_memory().total * mem_percent / 100

    # Allocate CPU load
    def cpu_stress():
        while True:
            for i in range(int(cpu_load)):
                x = i * i

    # Allocate memory load
    mem_stress = bytearray(int(mem_load))

    # Run the stress test for the specified duration
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_stress()
        time.sleep(0.1)

    # Release the allocated resources
    del mem_stress

# Run the stress test every 10 minutes
while True:
    cpu_mem_stress(90, 70, 300)  # 10% CPU, 10% RAM, 5 minutes
    print("Sleeping for 5 minutes...")
    time.sleep(300)
