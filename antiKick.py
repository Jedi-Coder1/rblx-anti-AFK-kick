from time import sleep
import win32gui, win32con
import pydirectinput as dirI

while True:
    sleep(6)
    print("Send Input To Roblox")
    hwnd = win32gui.FindWindowEx(None, None, None, "Roblox")
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(hwnd)
    dirI.press("esc")
    dirI.press("esc")
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)