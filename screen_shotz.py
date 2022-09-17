import pyautogui

# Takes screenshots continiously until stopped

indx = 0
while True:
    myScreenshot = pyautogui.screenshot()
    myScreenshot.save(f'screenshots\\screen_{indx}.png')
    indx += 1
    print(indx)