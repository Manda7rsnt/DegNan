import time
import webbrowser

total_breaks = 4
break_count = 0

print ("This script started on " + time.ctime())

while (break_count < total_breaks):
    time.sleep(20)
    webbrowser.open("https://www.youtube.com/watch?v=lEssh-ifWmo&list=RDlEssh-ifWmo")
    break_count = break_count +1
    
