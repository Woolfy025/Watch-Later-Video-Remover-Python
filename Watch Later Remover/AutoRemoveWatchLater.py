import pyautogui 
import time
import sys

    #uncomment the below code to find out where you need to click
    #it'll display the x and y in the terminal for you
    #comment it out again to run the rest of the script
    
#pyautogui.displayMousePosition()
#quit()

#set this count to however many videos you wanna delete off the list
count = 4000
for videos in range(count):
    try:
        #don't forget to change both of these sets of numbers
        #where the hamburger menu is
        pyautogui.moveTo(1396, 377)
        time.sleep(.5)
        pyautogui.click()
        #where the remove from watch later button is
        pyautogui.moveTo(1396, 500)
        time.sleep(.5)
        pyautogui.click()
    except KeyboardInterrupt:
        sys.exit()

