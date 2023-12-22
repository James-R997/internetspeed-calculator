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
        if user_input == "1":           # means the user chose to calculate the time of the download
            while True:
                try:
                    speed = float(input(f"{YELLOW}your internet speed {RED}(Mbps){YELLOW} > {DarkBLUE}"))
                    size = float(input(f"{YELLOW}your file size {RED}(Mbit){YELLOW} > {DarkBLUE}"))
                    break
                except ValueError:
                    print(f"{RED}invalid input.")
            calculate_time(size,speed)
            break

        elif user_input == "2":         # means the user chose to calculate the speed of the download
            while True:
                try:
                    time = float(input(f"{YELLOW}the time {RED}(seconds){YELLOW} > {DarkBLUE}"))
                    size = float(input(f"{YELLOW}your file size {RED}(Mbit){YELLOW} > {DarkBLUE}"))
                    break
                except ValueError:
                    print(f"{RED}invalid input.")
            calculate_speed(size, time)
            break
        
        elif user_input == "3":         # means the user chose to calculate the file size that was downloaded
            while True:
                try:
                    time = float(input(f"{YELLOW}the time {RED}(seconds){YELLOW} > {DarkBLUE}"))
                    speed = float(input(f"{YELLOW}your internet speed {RED}(Mbps){YELLOW} > {DarkBLUE}"))
                    break
                except ValueError:
                    print(f"{RED}invalid input.")
            calculate_fileSize(time, speed)
            break

        elif user_input.lower() == "help" or user_input.lower() == "h":     # to help the user
            print(f'''
            {PURPLE}    [1]{GREY} to calculate the time
            {PURPLE}    [2]{GREY} to calculate the speed
            {PURPLE}    [3]{GREY} to calculate the file size

            {PURPLE}        [Q]{GREY} to exit the code
            ''')
        
        elif user_input.lower() == "cls" or user_input.lower() == "clear":  # to clear the the text
            os.system("cls")
        
        elif user_input.lower() == "q" or user_input.lower() == "exit":     # to exit the program
            print(GREY)
            exit()
        
        else:                                                               # the user messed up
            print(f"{RED}invalid input, please choose one of the choices above")

    print(f"{GREY}\banything else?(type \"help\" to display the all the functions)")