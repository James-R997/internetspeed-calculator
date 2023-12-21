import os
from colors import *
from utilities import *

print(GREY) #to change the entire font color to grey

print(f'''
                W  E  L  C  O  M  E

        {PURPLE}    [1]{GREY} to calculate the time
        {PURPLE}    [2]{GREY} to calculate the speed
        {PURPLE}    [3]{GREY} to calculate the file size

        {PURPLE}        [Q]{GREY} to exit the code
''')

while True: #main loop

    while True: 
        user_input = input(f"{YELLOW}> {BLUE}")
        if user_input == "1":
            while True:
                try:
                    speed = int(input(f"{YELLOW}your internet speed {RED}(Mbps){YELLOW} > {DarkBLUE}"))
                    size = int(input(f"{YELLOW}your file size {RED}(Mbit){YELLOW} > {DarkBLUE}"))
                    break
                except ValueError:
                    print(f"{RED}invalid input.")
            calculate_time(size,speed)
            break

        elif user_input == "2":
            while True:
                try:
                    time = int(input(f"{YELLOW}the time {RED}(seconds){YELLOW} > {DarkBLUE}"))
                    size = int(input(f"{YELLOW}your file size {RED}(Mbit){YELLOW} > {DarkBLUE}"))
                    break
                except ValueError:
                    print(f"{RED}invalid input.")
            calculate_speed(size, time)
            break
        
        elif user_input == "3":
            while True:
                try:
                    time = int(input(f"{YELLOW}the time {RED}(seconds){YELLOW} > {DarkBLUE}"))
                    speed = int(input(f"{YELLOW}your internet speed {RED}(Mbps){YELLOW} > {DarkBLUE}"))
                    break
                except ValueError:
                    print(f"{RED}invalid input.")
            calculate_fileSize(time, speed)
            break

        elif user_input.lower() == "help" or user_input.lower() == "h":
            print(f'''
            {PURPLE}    [1]{GREY} to calculate the time
            {PURPLE}    [2]{GREY} to calculate the speed
            {PURPLE}    [3]{GREY} to calculate the file size

            {PURPLE}        [Q]{GREY} to exit the code
            ''')
        
        elif user_input.lower() == "cls" or user_input.lower() == "clear":
            os.system("cls")
        
        elif user_input.lower() == "q" or user_input.lower() == "exit":
            print(GREY)
            exit()
        
        else:
            print(f"{RED}invalid input, please choose one of the choices above")

    print(f"{GREY}\banything else?(type \"help\" to display the all the functions)")