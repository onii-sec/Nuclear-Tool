from os import name
from colorama import Fore, Style, init 
import socket, os, sys
from time import sleep

init()

os.system("title Nuclear tool")    # Title

def Clear():
    os.system("cls" if name == 'nt' else "clear")

def scan():
    print(Fore.MAGENTA + """
            _____                                 
           / ____|                                
          | (___   ___ __ _ _ __  _ __   ___ _ __ 
           \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
           ____) | (_| (_| | | | | | | |  __/ |   
          |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                            """) 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP Scan
    s.settimeout(3)                                        
    ip = input(Fore.CYAN + "Enter your ip address : ") 
    print(Fore.CYAN + "Your ip address " + ip + " is scanning...")
    for port in range(1, 1025):
        if s.connect_ex((ip, port)):
            print(Fore.RED + "[-] Port "+ str(port) +" is closed")
        else: 
            print(Fore.LIGHTGREEN_EX + "[+] The port is open")
print(Fore.BLUE + "End of the scan")
def exit():
    exit = input(Fore.BLUE + "To exit, press q : ")
    if exit == "q":
        sys.exit()
    

                                       

def Start():
    Clear()
    print(Fore.MAGENTA + """
                       

                ▄     ▄   ▄█▄    █     ▄███▄   ██   █▄▄▄▄        ▄▄▄▄▀ ████▄ ████▄ █     
                    █     █  █▀ ▀▄  █     █▀   ▀  █ █  █  ▄▀     ▀▀▀ █    █   █ █   █ █     
                ██   █ █   █ █   ▀  █     ██▄▄    █▄▄█ █▀▀▌          █    █   █ █   █ █     
                █ █  █ █   █ █▄  ▄▀ ███▄  █▄   ▄▀ █  █ █  █         █     ▀████ ▀████ ███▄  
                █  █ █ █▄ ▄█ ▀███▀      ▀ ▀███▀      █   █         ▀                      ▀ 
                █   ██  ▀▀▀                         █   ▀                                   
                                                ▀                                        
                                                                                                                
                        
                                         Press [t] for access the tool
                                       Made by Onii | Discord : Onii#0404          """)

    press = input(Fore.RED + "[>] : ")

    if press == "t":
        return
    elif press != "t":
        Start()

    
def printTitle():
    Clear()
    print(Fore.CYAN + Style.BRIGHT + """
                        $$\   $$\                     $$\                               
                        $$$\  $$ |                    $$ |                              
                        $$$$\ $$ |$$\   $$\  $$$$$$$\ $$ | $$$$$$\   $$$$$$\   $$$$$$\  
                        $$ $$\$$ |$$ |  $$ |$$  _____|$$ |$$  __$$\  \____$$\ $$  __$$\ 
                        $$ \$$$$ |$$ |  $$ |$$ /      $$ |$$$$$$$$ | $$$$$$$ |$$ |  \__|
                        $$ |\$$$ |$$ |  $$ |$$ |      $$ |$$   ____|$$  __$$ |$$ |      
                        $$ | \$$ |\$$$$$$  |\$$$$$$$\ $$ |\$$$$$$$\ \$$$$$$$ |$$ |      
                        \__|  \__| \______/  \_______|\__| \_______| \_______|\__|      
                                                                                        
                                                                                        """)
    print(Fore.WHITE + """                               ____________________________________________
            
                                    1 : Port Scanner      2 : Coming soon 
                                    
                                    3 : Coming soon       4 : Coming soon
                                    
                                ____________________________________________  """)

    n = int(input(Fore.RED +"Choose a number :"))

    if n == 1:
        Clear()
        scan()
    else:
        Clear()
        printTitle()

    def main():
        print()

    if __name__ == '__main__':
        main()
Start()
printTitle()





