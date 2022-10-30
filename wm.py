import win32gui
import win32com.client
from pynput import keyboard


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        ctx.append((hwnd, win32gui.GetWindowText(hwnd)))


top_window = []
win32gui.EnumWindows(winEnumHandler, top_window)
x = 0
for i in top_window:
    x += 1
    print(x, i)


while True:
    s = -1
    with keyboard.Events() as events:
        # Block for as much as possible
        event = events.get(1e6)
        if event.key == keyboard.KeyCode.from_char('0'):
            s = 0
        elif event.key == keyboard.KeyCode.from_char('1'):
            s = 1
        elif event.key == keyboard.KeyCode.from_char('2'):
            s = 2
        elif event.key == keyboard.KeyCode.from_char('3'):
            s = 3
        elif event.key == keyboard.KeyCode.from_char('4'):
            s = 4
        elif event.key == keyboard.KeyCode.from_char('5'):
            s = 5
        elif event.key == keyboard.KeyCode.from_char('6'):
            s = 6
        elif event.key == keyboard.KeyCode.from_char('7'):
            s = 7
        elif event.key == keyboard.KeyCode.from_char('8'):
            s = 8
        elif event.key == keyboard.KeyCode.from_char('9'):
            s = 9
        if (s != -1):
            w = (top_window[s-1])
            print(w)
            shell = win32com.client.Dispatch("WScript.Shell")
            shell.SendKeys('%')
            win32gui.ShowWindow(w[0], 5)
            win32gui.SetForegroundWindow(w[0])
    pass
