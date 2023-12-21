from colors import *

def calculate_time(size, speed):
    time = (size/speed)
    if time > 60:
        time = round(time/60)
        return print(f"{BLUE}the time is around {RED}" + str(time) + f"{BLUE} minutes.")
    elif time < 1:
        return print(f"{BLUE}the time is less than {RED}" + "1" + f"{BLUE} second.")
    else:
        time = round(time)
        return print(f"{BLUE}the time is around {RED}" + str(time) + f"{BLUE} seconds.")

    
def calculate_speed(size, time):
    speed = str(round(size/time)) #Mbit/s
    return print(f"{BLUE}the speed is around {RED}" + speed + f"{BLUE} Mbps.")

def calculate_fileSize(time, speed):
    size = str(time*speed) #Mbit
    return print(f"{BLUE}the size is around {RED}" + size + f"{BLUE} Mbit.")