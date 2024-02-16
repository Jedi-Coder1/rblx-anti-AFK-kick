from time import sleep
import win32gui, win32con
try:
    import pydirectinput as dirI
except ImportError:
    print("missing imports! please run 'pip install PyDirectInput' in a terminal")

willClick = True
# change to ^ False if you want it to press a key instead
key = None
# change ^ to which key you want to be pressed (list of acceptable keys "https://gist.github.com/Jedi-Coder1/395d45c0dfa3f3001bc7f8adaa72e064")

while True:
    sleep(1140)
    # Get Window Handle
    hwnd = win32gui.FindWindowEx(None, None, None, "Roblox")
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)
    win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)
    win32gui.SetForegroundWindow(hwnd)
    if willClick:
        dirI.click()
    else:
        if key:
            dirI.press(key)
        else:
            print("please provide a key to press")
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)