import pyautogui
import time


print("hover over the color you want to grab, then press ENTER.")
input()


x,y = pyautogui.position()
x = x * 2
y = y * 2
print(f"mouse coordinates: {x} and {y}")
print(pyautogui.pixel(x,y))



