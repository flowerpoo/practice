import psutil

#count the number of cpu in machine
cpu_count = psutil.cpu_count()
print("Monitoring CPU usage...")
def monitor():
    try:
        while True:
            a= psutil.cpu_percent(cpu_count)
            #start if loop when cpu performance greater than 80
            if( a >= 8):
                print(f"Alert! CPU usage exceeds threshold: {a}%")
        #it will run continuously until the interrupt happens
    finally: # once click Ctr+c it will gives a msg and end the process.
        print("monitoring stoped")

monitor()