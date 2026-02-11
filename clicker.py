import pyautogui, time, threading, random, pydivert, keyboard, win32gui, ctypes
from win32gui import GetForegroundWindow, GetPixel, GetDC, GetWindowRect
from win32api import PostMessage, MAKELONG
from win32con import WM_MOUSEMOVE, WM_LBUTTONDOWN, WM_LBUTTONUP, WM_CHAR, WM_KEYDOWN, WM_KEYUP

user32 = ctypes.windll.user32

active_threads = []

status = True
clicker_on_off = False

keys = {
    'lbutton':1,
    'rbutton':2,
    'cancel':3,
    'mbutton':4,
    'x1button':5,
    'x2button':6,
    'back':8,
    'tab':9,
    'clear':12,
    'return':13,
    'esc':27,
    'left':37,
    'up':38,
    'right':39,
    'down':40,
    'a':65,
    'b':66,
    'c':67,
    'd':68,
    'e':69,
    'f':70,
    'g':71,
    'h':72,
    'i':73,
    'j':74,
    'k':75,
    'l':76,
    'm':77,
    'n':78,
    'o':79,
    'p':80,
    'q':81,
    'r':82,
    's':83,
    't':84,
    'u':85,
    'v':86,
    'w':87,
    'x':88,
    'y':89,
    'z':90,
    'numpad0':96,
    'numpad1':97,
    'numpad2':98,
    'numpad3':99,
    'numpad4':100,
    'numpad5':101,
    'numpad6':102,
    'numpad7':103,
    'numpad8':104,
    'numpad9':105,
    'f1':112,
    'f2':113,
    'f3':114,
    'f4':115,
    'f5':116,
    'f6':117,
    'f7':118,
    'f8':119,
    'f9':120,
    'f10':121,
    'f11':122,
    'f12':123,
    'f13':124,
    'f14':125,
    'f15':126,
    'f16':127,
    'f17':128,
    'f18':129,
    'f19':130,
    'f20':131,
    'f21':132,
    'f22':133,
    'f23':134,
    'f24':135,
    'lshift':160,
    'rshift':161,
    'lcontrol':162,
    'rcontrol':163,
}

def getkeystate(keycode):
    if user32.GetKeyState(keycode) & 32768:
        return True
    return False


def all_pressed(keycode_args):
    for key in keycode_args:
        if not getkeystate(key):
            return False

    return True

def any_pressed(keycode_args):
    for key in keycode_args:
        if getkeystate(key):
            return True

    return False

def get_hotkey(key):
    for i in keys:
        if str(key) == str(i):
            return keys[str(i)]


def get_random_ms(min1, max1):
    return random.randint(min1, max1)

def calculate_ms(ms):
    calc = ms / 3
    min = ms + calc
    return min

def clicker_standard(hotkey, ms):
    global status
    
    while clicker_on_off == True:
        while status == True:
            if getkeystate(int(get_hotkey('lbutton'))):
                PostMessage(GetForegroundWindow(), 0x201, 1)
                PostMessage(GetForegroundWindow(), 0x202, 0)
                time.sleep(float(ms / 1000))
                if getkeystate(int(get_hotkey(str(hotkey)))):
                    status = False
                    time.sleep(0.3)
                if clicker_on_off == False:
                    break
            if getkeystate(int(get_hotkey('e'))) or getkeystate(int(get_hotkey('esc'))):
                if status == True:
                    status = False
                    while True:
                        if getkeystate(int(get_hotkey('e'))) or getkeystate(int(get_hotkey('esc'))):
                            status = True
                            break
            if getkeystate(int(get_hotkey(str(hotkey)))):
                status = False
                time.sleep(0.3)
            if clicker_on_off == False:
                break
        while status == False:
            if getkeystate(int(get_hotkey(str(hotkey)))):
                status = True
                time.sleep(0.3)
            if clicker_on_off == False:
                break

def clicker_randomize(hotkey, ms):
    global status
    while clicker_on_off == True:
        while status == True:
            if getkeystate(int(get_hotkey('lbutton'))):#1
                PostMessage(GetForegroundWindow(), 0x201, 1)
                PostMessage(GetForegroundWindow(), 0x202, 0)
                x = float(int(get_random_ms(ms, cps_calc)) / 1000)
                time.sleep(x)
                if getkeystate(int(get_hotkey(str(hotkey)))):
                    status = False
                    time.sleep(0.3)
                if clicker_on_off == False:
                    break
            if getkeystate(int(get_hotkey('e'))) or getkeystate(int(get_hotkey('esc'))):
                if status == False:
                    status = True
                else:
                    status = False
            if getkeystate(int(get_hotkey(str(hotkey)))):
                status = False
                time.sleep(0.3)
            if clicker_on_off == False:
                break
        while status == False:
            if getkeystate(int(get_hotkey(str(hotkey)))):
                status = True
                time.sleep(0.3)
            if clicker_on_off == False:
                break

def check_for_eq():
    global status
    while clicker_on_off == True:
        if getkeystate(int(get_hotkey('e'))) or getkeystate(int(get_hotkey('esc'))):
            status = False
            time.sleep(0.2)

def clicker_garda(ms):
    global status
    while clicker_on_off == True:
        while status == True:
            if getkeystate(int(get_hotkey('lbutton'))):
                pyautogui.click(button='right')
                time.sleep(float(ms / 1000))
            if clicker_on_off == False:
                break
        while status == False:
            time.sleep(0.1)
            if clicker_on_off == False:
                break
            pass
        if clicker_on_off == False:
            break

def fake_lag(moc, button):
    wd = pydivert.WinDivert('tcp.DstPort < 30549 and tcp.DstPort > 20549')
    while clicker_on_off == True:
        if getkeystate(keys[button]):
            wd.open()
            while getkeystate(keys[button]) >> int(moc):
                packet = wd.recv()
                time.sleep(0.5)
                wd.send(packet)
            wd.close()
        time.sleep(0.01)
        if clicker_on_off == False:
            break

def sniezka(slot, miecz, button):
    while clicker_on_off == True:
        if getkeystate(keys[button]):
            keyboard.press_and_release(slot)
            time.sleep(0.1)
            PostMessage(GetForegroundWindow(), 0x204, 1)
            PostMessage(GetForegroundWindow(), 0x205, 0)
            time.sleep(0.1)
            keyboard.press_and_release(miecz)
            time.sleep(0.2)
        if clicker_on_off == False:
            break
        time.sleep(0.1)


def punch(slot, button):
    while clicker_on_off == True:
        if keyboard.is_pressed(button):
            keyboard.press_and_release(slot)
            time.sleep(0.1)
            PostMessage(GetForegroundWindow(), 0x204, 1)
            time.sleep(0.1)
            PostMessage(GetForegroundWindow(), 0x205, 0)
            time.sleep(0.1)
            keyboard.press_and_release(slot)
            time.sleep(0.4)
        if clicker_on_off == False:
            break


def custom_komenda(komenda, button):
    while clicker_on_off == True:
        if getkeystate(keys[button]):
            keyboard.press_and_release('t')
            time.sleep(0.1)
            for letter in komenda:
                keyboard.press_and_release(str(letter))
                time.sleep(0.05)
            keyboard.press_and_release('enter')
        if clicker_on_off == False:
            break

def zmiana_seta(time_change, button, slots):
    while clicker_on_off == True:
        if getkeystate(keys[button]):
            hwnd = win32gui.GetForegroundWindow()
            rect = win32gui.GetWindowRect(hwnd)
            w = rect[2] - rect[0]
            h = rect[3] - rect[1]
            threading.Thread(target=scaling, args=((rect[2] - rect[0] - 16), (rect[3] - rect[1] - 39), hwnd, time_change, slots,)).start()
            time.sleep(0.1)

def get_pixel_color(hwnd, x, y):
    dc = GetDC(None)
    window_rect = GetWindowRect(int(hwnd))
    clr = GetPixel(dc, int(x+int(window_rect[0])), int(y+int(window_rect[1])))
    if clr == 2171169:
        return 'match'
    else:
        return 'not'

def change_part(row_start_pos, grid_start_pos, xd, pozx, pozy, hwnd, time_change):
    PostMessage(int(hwnd), WM_MOUSEMOVE, 0, MAKELONG(int(int(row_start_pos)+(pozx)*36), int(grid_start_pos)+int(4+pozy)*36+8))
    PostMessage(int(hwnd), WM_LBUTTONDOWN, 0x201, 1|0x00000001)
    PostMessage(int(hwnd), WM_LBUTTONUP, 0x202, 1|0xC0000001)
    time.sleep(time_change)
    PostMessage(int(hwnd), WM_MOUSEMOVE, 0, MAKELONG(int(row_start_pos), int(grid_start_pos)+(xd)*36))
    PostMessage(int(hwnd), WM_LBUTTONDOWN, 0x201, 1|0x00000001)
    PostMessage(int(hwnd), WM_LBUTTONUP, 0x202, 1|0xC0000001)
    time.sleep(time_change)
    PostMessage(int(hwnd), WM_MOUSEMOVE, 0, MAKELONG(int(int(row_start_pos)+(pozx)*36), int(grid_start_pos)+int(4+pozy)*36+8))
    PostMessage(int(hwnd), WM_LBUTTONDOWN, 0x201, 1|0x00000001)
    PostMessage(int(hwnd), WM_LBUTTONUP, 0x202, 1|0xC0000001)
    time.sleep(time_change)

def scaling(x, y, hwnd, time_change, slots):

    if y < 480 or x < 640:
        pass
    else:
        xpos = x / 2 - (348 / 2)
        ypos = y / 2 - (328 / 2)
        row_start_pos = xpos + 29
        grid_start_pos = ypos + 29
        PostMessage(int(hwnd), WM_KEYDOWN, 0x45, 1|0x00000001)
        PostMessage(int(hwnd), WM_CHAR, 0x45, 0)
        PostMessage(int(hwnd), WM_KEYUP, 0x45, 1|0xC0000001)
        time.sleep(0.1)

        parts_list = []
        for s in slots:
            if s > 8:
                py = int(s / 9)
                px = s - int(9 * py)
                pl = [py, px]
                parts_list.append(pl)
            else:
                py = 0
                px = s
                pl = [py, px]
                parts_list.append(pl)
        i = 0
        for s in parts_list:
            change_part(row_start_pos, grid_start_pos, i, s[1], s[0], hwnd, time_change)
            i += 1
        PostMessage(int(hwnd), WM_KEYDOWN, 0x45, 1|0x00000001)
        PostMessage(int(hwnd), WM_CHAR, 0x45, 0)
        PostMessage(int(hwnd), WM_KEYUP, 0x45, 1|0xC0000001)

def stop_all_threads():
    for thread in active_threads:
    #    thread.terminate()
        pass

def start_clicker(clicker_ms, clicker_button, garda, garda_ms, fakelag, moc, fakelag_button, zmiana_seta_check, zmiana_seta_slots, zmiana_seta_time, zmiana_seta_button, komenda, komenda_text, komenda_button, sniezka_bool, sniezka_slot_miecz, sniezka_slot_sniezka, sniezka_button, mode):
    global cps_calc, active_threads
    cps_calc = int(calculate_ms(clicker_ms))

    if mode == False:
        clicker_standard_thread = threading.Thread(target=clicker_standard, args=(clicker_button, clicker_ms, )).start()
        active_threads.append(clicker_standard_thread)
        if garda == True:
            clicker_garda_thread = threading.Thread(target=clicker_garda, args=(garda_ms,)).start()
            active_threads.append(clicker_garda_thread)
        if fakelag == True:
            fake_lag_thread = threading.Thread(target=fake_lag, args=(moc, fakelag_button,)).start()
            active_threads.append(fake_lag_thread)
        if sniezka_bool == True:
            sniezka_thread = threading.Thread(target=sniezka, args=(sniezka_slot_sniezka, sniezka_slot_miecz, sniezka_button,)).start()
            active_threads.append(sniezka_thread)
        if komenda == True:
            custom_komenda_thread = threading.Thread(target=custom_komenda, args=(komenda_text, komenda_button,)).start()
            active_threads.append(custom_komenda_thread)
        if zmiana_seta_check == True:
            zmiana_seta_thread = threading.Thread(target=zmiana_seta, args=(zmiana_seta_time,zmiana_seta_button,zmiana_seta_slots,)).start()
            active_threads.append(zmiana_seta_thread)
        threading.Thread(target=check_for_eq).start()
    elif mode == True:
        threading.Thread(target=clicker_randomize, args=(clicker_button, clicker_ms,)).start()
        if garda == True:
            threading.Thread(target=clicker_garda, args=(garda_ms,)).start()
        if fakelag == True:
            threading.Thread(target=fake_lag, args=(moc, fakelag_button,)).start()
        if sniezka_bool == True:
            threading.Thread(target=sniezka, args=(sniezka_slot_sniezka, sniezka_slot_miecz, sniezka_button,)).start()
        if komenda == True:
            threading.Thread(target=custom_komenda, args=(komenda_text, komenda_button,)).start()
        if zmiana_seta_check == True:
            threading.Thread(target=zmiana_seta, args=(zmiana_seta_time,zmiana_seta_button,)).start()