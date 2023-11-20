import pyautogui
import time

a=input('What do u wanna print?: ') #word to be broken down
b=len(a)
t=int(input('Enter the time delay you want before execution (in seconds): ')) #delay
time.sleep(t)
count=0

for i in range(b):
    pyautogui.typewrite(a[i])
    pyautogui.press('enter')
    count+=1

print('Job completed succesffully!') #confirmation message
