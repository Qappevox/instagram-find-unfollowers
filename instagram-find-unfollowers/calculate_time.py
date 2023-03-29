import time

def timer(param):
    delta = 0
    start_time = time.time()
    while (delta < param):
        end_time = time.time()
        delta = end_time - start_time
        print("time remaining -->" +str(param- delta))
    return False
