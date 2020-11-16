import pyautogui, time

time.sleep(5) #so it doesn't start spamming right away

i = 0

while i < 50:

    f = open("marine.txt", "r")

    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
    
    f.close()
    i += 1
    time.sleep(4) #only needed for big amounts of text

