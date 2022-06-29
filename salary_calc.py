import ctypes
import sys, time, os
import colorama
from colorama import Fore, Back, Style
os.system("cls")
colorama.init()

ctypes.windll.kernel32.SetConsoleTitleW("salary calculator") #sets the console title

developer = "\033[31mDeveloped by ! J#2389 in Python | <33"

print()

for char in developer:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

while True:
    
    print()
    print()
    print(f"{Fore.BLUE}███████╗ █████╗ ██╗      █████╗ ██████╗ ██╗   ██╗     ██████╗ █████╗ ██╗      ██████╗██╗   ██╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ")
    print(f"{Fore.BLUE}██╔════╝██╔══██╗██║     ██╔══██╗██╔══██╗╚██╗ ██╔╝    ██╔════╝██╔══██╗██║     ██╔════╝██║   ██║██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
    print(f"{Fore.BLUE}███████╗███████║██║     ███████║██████╔╝ ╚████╔╝     ██║     ███████║██║     ██║     ██║   ██║██║     ███████║   ██║   ██║   ██║██████╔╝")
    print(f"{Fore.BLUE}╚════██║██╔══██║██║     ██╔══██║██╔══██╗  ╚██╔╝      ██║     ██╔══██║██║     ██║     ██║   ██║██║     ██╔══██║   ██║   ██║   ██║██╔══██╗")
    print(f"{Fore.BLUE}███████║██║  ██║███████╗██║  ██║██║  ██║   ██║       ╚██████╗██║  ██║███████╗╚██████╗╚██████╔╝███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║")
    print(f"{Fore.BLUE}╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝" + Fore.RESET)
    print()
    print(f"{Fore.RED}(To fix the appereance bug above, make the program a little wider! (<->))" + Fore.RESET)


    hourly_wage = float(input("\nEnter your hourly wage ($): "))
    weekly_working_time = float(input("Enter your weekly working hours: "))
    years = float(input("For how many years do you want to calculate your salary: "))

    if years == 0:
        annual_salary = hourly_wage * weekly_working_time * 13 / 3 * 12 * years
        print("\nWith a hourly wage of " + str(hourly_wage) + "$ and a weekly working time of " + str(weekly_working_time) + " hours, you earn " + str(annual_salary) + "$ in " + str(years) + " years.")
    elif years <= 1:
        annual_salary = hourly_wage * weekly_working_time * 13 / 3 * 12 * years
        print("\nWith a hourly wage of " + str(hourly_wage) + "$ and a weekly working time of " + str(weekly_working_time) + " hours, you earn " + str(annual_salary) + "$ in " + str(years) + " year.")
    else:
        annual_salary = hourly_wage * weekly_working_time * 13 / 3 * 12 * years
        print("\nWith a hourly wage of " + str(hourly_wage) + "$ and a weekly working time of " + str(weekly_working_time) + " hours, you earn " + str(annual_salary) + "$ in " + str(years) + " years.")

    print()

    again = str(input("Do you want to calculate something again (y/n): "))

    if again == "y":
        os.system("cls")
        continue
    elif again == "n":
        print("\nclosing this program in 3 seconds.")
        time.sleep(3) #waits for 3 secs, you HAVE TO 'import time'
        exit(0) #closes the program
    else:
        print("\nInvalid choice.")
        print("\nclosing this program in 3 seconds.")
        time.sleep(3) #waits for 3 secs, you HAVE TO 'import time'
        exit() #closes the program
        
            