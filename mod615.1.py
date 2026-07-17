#15.1
#Use multiprocessing to create three separate processes. Make each one wait a random number of seconds between zero and one, print the current time, and then exit.
import multiprocessing
import random
import time

from datetime import datetime

def worker():
    pause = random.randrange(0,1)
    time.sleep(pause)
    print_time = datetime.now().strftime("%H:%M:%S.%f")
    print(f"Process waited{pause:.4f}seconds, current:{print_time}")

if __name__ == "__main__":
    processes = []

    for i in range(3):
        p = multiprocessing.Process(target=worker)
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

    print("All processes finished.")
    
