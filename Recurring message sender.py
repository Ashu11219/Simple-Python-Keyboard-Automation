import pyautogui
import time

a=input('What do u wanna print?: ') #the message you want to send
n=int(input('How many times?: ')) #number of repititions
t=int(input('Enter the time delay you want between each message (in seconds): ')) #delay
time.sleep(3)
count=0

for i in range(1,n+1):
    pyautogui.typewrite(a)
    pyautogui.press('enter')
    time.sleep(t)
    count+=1

print('Job completed succesffully!') #confirmation message

