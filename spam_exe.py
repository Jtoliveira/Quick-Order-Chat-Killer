import pyautogui, time

from tkinter import *

def run():
    time.sleep(5) #so it doesn't start spamming right away

    i = 0

    words = textInput.get().split()

    while i < int(repetitions.get()):

        for word in words:
            pyautogui.typewrite(word + " ")
        
        pyautogui.press("enter")
        i += 1

root = Tk()
root.title("Quick Order Chat Killer")
root.geometry("600x600")

textInput = Entry(root)

textInput.insert(0, "Sample Text")

repetitions = Entry(root)
repetitions.insert(0, "5")

warning = Label(root, text="You have 5 seconds to set the cursor in the right window after pressing the button")

submitButton = Button(root, text="Start", command = run)

textInput.pack()
repetitions.pack()
warning.pack()
submitButton.pack()


root.mainloop()

