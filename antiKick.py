from time import sleep
import win32gui, win32con
try:
    import pydirectinput as dirI
except ImportError:
    print("missing imports! please run 'pip install PyDirectInput' in a terminal")

while True:
    sleep(1150)
    print("Send Input To Roblox")
    hwnd = win32gui.FindWindowEx(None, None, None, "Roblox")
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(hwnd)
    dirI.press("esc")
    dirI.press("esc")
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)