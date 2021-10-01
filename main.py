import threading
from termcolor  import colored
from pyfiglet import Figlet


f = Figlet(font='isometric2')
print(f.renderText('SLAC'))
min = 0


def introduction():
    print(
        "Welcome Champ!"
    )
    print(
        "-"*60
    )
    print(
        "This software will help you to stand up by reminding you occasionally.\nAll you have to do is to specify one thing:\n1-How many minutes do you want to stand for every hour. (Recommended 15 minutes). \nIt's that simple!. It will dissappear the moment you enter the required information. It will pop off the moment you specified.\nKeep the hard work champ and good luck!"
    )
    print(
        "-"*60
    )
    
    return input("Enter min: ")





def standing():
    print("Standing time baby!")
    standingTimer = threading.Timer(int(min)*60,sitting)
    standingTimer.start()

def sitting():
    print("U can sit now. GOOD JOB !")
    workingTimer = threading.Timer(60*60, standing)
    workingTimer.start()

min = introduction()
firstTime = threading.Timer(60*60,standing)
firstTime.start()

