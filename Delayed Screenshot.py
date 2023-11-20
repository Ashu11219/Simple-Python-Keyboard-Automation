import pyautogui
import time

x=input('Are you ready? (y/n): ') #asking confirmation
t=int(input('How much time? (in seconds): ')) #delay

if(x=='y'):
    time.sleep(t)
    pyautogui.press('prntscrn')

print('Job completed succesffully!') #confirmation message