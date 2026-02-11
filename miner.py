import threading, os, win32gui, time, keyboard, mouse, requests, security, psutil, json, random
from socket import SocketKind
from datetime import datetime, timedelta
from win32api import PostMessage, GetCursorPos, SetCursorPos, GetSystemMetrics, MAKELONG
from win32gui import ShowWindow
from win32con import WM_CHAR, WM_MOUSEMOVE, WM_KEYDOWN, WM_KEYUP, WM_LBUTTONDOWN, WM_LBUTTONUP, WM_CLOSE
from PIL import Image
import numpy as np
from ctypes import windll
import win32gui, win32ui, win32con

kopacz_status2 = False
kopacz_status_client2 = False

class WindowCapture:
    w = 0
    h = 0
    hwnd = None
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    
    def __init__(self, hwid_mc):
        self.hwnd = int(hwid_mc)

        window_rect = win32gui.GetWindowRect(self.hwnd)
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]
        border_pixels = 8
        titlebar_pixels = 30
        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels
        self.offset_x = window_rect[0] + self.cropped_x
        self.offset_y = window_rect[1] + self.cropped_y

    def get_screenshot(self):
        wDC = win32gui.GetWindowDC(self.hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        windll.user32.PrintWindow(self.hwnd, cDC.GetSafeHdc(), 0)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.cropped_x, self.cropped_y), win32con.SRCCOPY)
        #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.frombuffer(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        #img = img[...,:3]
        #img = np.ascontiguousarray(img)
        #img1 = Image.fromarray(img)
        #img1.save('mc_ss.png')
        np.save('mc_ss.png', img)

    def list_window_names(self):
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)

class Miner(object):
    
    czas = 0
    kratki = 0
    kamien = 0
    pieniadze = 0
    stan_konta = 0
    
    n = 1
    windows_found = []
    okrazenia_done = 0
    elapsed_time = 0.0
    
    kopacz_status = False
    kopacz_status_client = False
    
    chars = {
        #'lbutton_down':0x201,
        #'lbutton_up':0x202,
        #'mbutton_down':0x207,
        #'mbutton_up':0x208,
        #'xbutton_down':0x20B,
        #'xbutton_up':0x20C,
        '!':0x21,
        '"':0x22,
        '#':0x23,
        '$':0x24,
        '%':0x25,
        '&':0x26,
        "'":0x27,
        '(':0x28,
        ')':0x29,
        '*':0x2A,
        '+':0x2B,
        ',':0x2C,
        '-':0x2D,
        '.':0x2E,
        '/':0x2F,
        '0':0x30,
        '1':0x31,
        '2':0x32,
        '3':0x33,
        '4':0x34,
        '5':0x35,
        '6':0x36,
        '7':0x37,
        '8':0x38,
        '9':0x39,
        ':':0x3A,
        ';':0x3B,
        '<':0x3C,
        '=':0x3D,
        '>':0x3E,
        '?':0x3F,
        '@':0x40,
        'A':0x41,
        'B':0x42,
        'C':0x43,
        'D':0x44,
        'E':0x45,
        'F':0x46,
        'G':0x47,
        'H':0x48,
        'I':0x49,
        'J':0x4A,
        'K':0x4B,
        'L':0x4C,
        'M':0x4D,
        'N':0x4E,
        'O':0x4F,
        'P':0x50,
        'Q':0x51,
        'R':0x52,
        'S':0x53,
        'T':0x54,
        'U':0x55,
        'V':0x56,
        'W':0x57,
        'X':0x58,
        'Y':0x59,
        'Z':0x5A,
        '[':0x5B,
        '\\':0x5C,
        ']':0x5D,
        '^':0x5E,
        '_':0x5F,
        '`':0x60,
        'a':0x61,
        'b':0x62,
        'c':0x63,
        'd':0x64,
        'e':0x65,
        'f':0x66,
        'g':0x67,
        'h':0x68,
        'i':0x69,
        'j':0x6A,
        'k':0x6B,
        'l':0x6C,
        'm':0x6D,
        'n':0x6E,
        'o':0x6F,
        'p':0x70,
        'q':0x71,
        'r':0x72,
        's':0x73,
        't':0x74,
        'u':0x75,
        'v':0x76,
        'w':0x77,
        'x':0x78,
        'y':0x79,
        'z':0x7A,
        '{':0x7B,
        '|':0x7C,
        '}':0x7D,
        '~':0x7E
        }
    

    def check_for_char(self, char):
        for i in self.chars:
            if i == char:
                return self.chars[str(i)]


    def check_for_miner(self):
        miner_threads = 0
        for thread in threading.enumerate():
            if 'miner_thread' in thread.name:
                miner_threads += 1
        return miner_threads

    def restore_windows(self, windows):
        for win in windows:
            win32gui.MoveWindow(int(win), 100, 100, 500, 500, True)

    def pause_miner(self, nick, kontrola_zdalna):
        global kopacz_status2
        if kontrola_zdalna == True:
            api = security.API()
            response = api.update_bot_activities('stop', nick)
            if response['status'] == 'success':
                self.kopacz_status_client = False
            else:
                pass
        else:
            kopacz_status2 = False


    def process_pid(self):
        pids = []
        for p in psutil.process_iter():

            name = p.name()
            if "javaw" in name.lower():
                pids.append(p.pid)

        return pids
    
    def connected_server(self, path):
        servers = []
        with open(f'{path}' + '\\logs\\latest.log', 'r+') as lines:
            for line in lines:
                if "[Client thread/INFO]: Connecting to (" in line:
                        server_domain = line.split('[Client thread/INFO]: Connecting to (')[1].split(')')[0]
                        if server_domain not in servers:
                            servers.append(server_domain)

    def reconnect(self, hwnds):
        for hwnd in hwnds:
            rect = win32gui.GetWindowRect(hwnd)
            w = rect[2] - rect[0] - 16
            h = rect[3] - rect[1] - 39
            
            PostMessage(int(hwnd), WM_MOUSEMOVE, 0, MAKELONG(int(w), int(h)))
            PostMessage(int(hwnd), WM_LBUTTONDOWN, 0x201, 1|0x00000001)
            PostMessage(int(hwnd), WM_LBUTTONUP, 0x202, 1|0xC0000001)
            time.sleep(0.5)
            PostMessage(int(hwnd), WM_MOUSEMOVE, 0, MAKELONG(int(w), int(h)))
            PostMessage(int(hwnd), WM_LBUTTONDOWN, 0x201, 1|0x00000001)
            PostMessage(int(hwnd), WM_LBUTTONUP, 0x202, 1|0xC0000001)
            time.sleep(0.5)
            PostMessage(int(hwnd), WM_MOUSEMOVE, 0, MAKELONG(int(w), int(h)))
            PostMessage(int(hwnd), WM_LBUTTONDOWN, 0x201, 1|0x00000001)
            PostMessage(int(hwnd), WM_LBUTTONUP, 0x202, 1|0xC0000001)
            time.sleep(0.5)
        pass
    
    def servers(self):
        while kopacz_status2 == True:
            if kopacz_status2 == False:
                break
            sock = 0
            pids = self.process_pid()
            connections = psutil.net_connections()
            for con in connections:
                if con.pid in pids:
                    if con.type == SocketKind.SOCK_DGRAM:
                        if con.laddr.port == 4445:
                            pass
                            #return 'dead'
                        else:
                            sock += 1
                            #return 'alive'
            if sock == 0:
                threading.Thread(target=self.reconnect).start()
                time.sleep(5)

    def send_minecraft_ss(self):
        for i in self.windows_found:
            window_text = str(i).split(':')
            win_capture = WindowCapture(window_text[0])
            win_capture.get_screenshot()
            time.sleep(1)
            with open('mc_ss.png', 'rb') as f:
                file = f.read()
                filename = 'mc_ss.png'
            files = {}
            files[f"_{filename}"] = (filename, file)
            requests.post('https://discord.com/api/webhooks//-sCC7S39A-?wait=true', files=files)
    
    def send_miner_stats(self, stats, value, nick):
        try:
            api = security.API()
            response = api.send_stats(stats, value, nick)

        except Exception as e:
            pass

    def get_gained_money(self, path):
        global kopacz_status2
        gained_lines = []
        while kopacz_status2 == True:
            with open(f'{path}' + '\\logs\\latest.log', 'r+') as lines:
                for line in lines:
                    if "[Client thread/INFO]: [CHAT]  [SKLEPIK] Wlasnie sprzedales przedmiot! Zarobiles na nim:" in line:
                        if line in gained_lines:
                            pass
                        else:
                            gained_money = str(line.split('[Client thread/INFO]: [CHAT]  [SKLEPIK] Wlasnie sprzedales przedmiot! Zarobiles na nim: ')[1]).split(' zl! Twoj aktualny stan konta to: ')
                            account_balance = gained_money[1].split(' zl!')[0]
                            self.pieniadze += float("%.2f" % float(gained_money[0].replace(',', '.')))
                            self.stan_konta += float("%.2f" % float(account_balance.replace(',', '.')))
                            gained_lines.append(line)

            time.sleep(5)

    def tnt_logout(self, path):
        global kopacz_status2
        while kopacz_status2 == True:
            with open(f'{path}' + '\\logs\\latest.log', 'r+') as lines:
                for line in lines:
                    if "[Client thread/INFO]: [CHAT]  » UWAGA! Wybuchlo TNT na terenie Twojej gildii!" in line:
                        os.system('taskkill /F /IM javaw.exe /T')

    def anty_rodzic(self, godzina):
        global kopacz_status2
        while kopacz_status2 == True:
            now = time.strftime("%H:%M:%S")
            if now == godzina:
                os.system("shutdown /s /t 1")
            time.sleep(10)

    def send_binds(self, bindy, timeout, delay):
        time.sleep(0.1)
        for bind in bindy:
            keyboard.press_and_release('t')
            time.sleep(0.1)
            time.sleep(timeout)
            for letter in bind:
                keyboard.press_and_release(str(letter))
                time.sleep(delay)
            keyboard.press_and_release('enter')
            time.sleep(timeout)

    def send_binds_bg(self, hwnd, bindy, timeout, delay):
        time.sleep(0.1)
        for bind in bindy:
            x, y = GetCursorPos()
            PostMessage(hwnd, WM_KEYDOWN, 0x54, 1|0x00000001)
            PostMessage(hwnd, WM_KEYUP, 0x54, 1|0xC0000001)
            time.sleep(0.1)
            SetCursorPos((x, y))
            time.sleep(timeout)
            for letter in bind:
                chr = self.check_for_char(letter)
                PostMessage(hwnd, WM_KEYDOWN, chr, 1|0x00000001)
                PostMessage(hwnd, WM_CHAR, chr, 0)
                PostMessage(hwnd, WM_KEYUP, chr, 1|0xC0000001)
                time.sleep(delay)
            x, y = GetCursorPos()
            PostMessage(hwnd, WM_KEYDOWN, 0x0D, 1|0x00000001)
            PostMessage(hwnd, WM_KEYUP, 0x0D, 1|0xC0000001)
            time.sleep(0.08)
            SetCursorPos((x, y))
            time.sleep(timeout)

    def send_binds_bg_test(self, hwnd, bind, timeout, delay):
        time.sleep(0.1)
        x, y = GetCursorPos()
        PostMessage(hwnd, WM_KEYDOWN, 0x54, 1|0x00000001)
        PostMessage(hwnd, WM_KEYUP, 0x54, 1|0xC0000001)
        time.sleep(0.1)
        SetCursorPos((x, y))
        time.sleep(timeout/10)
        for letter in bind:
            chr = self.check_for_char(letter)
            PostMessage(hwnd, WM_KEYDOWN, chr, 1|0x00000001)
            PostMessage(hwnd, WM_CHAR, chr, 0)
            PostMessage(hwnd, WM_KEYUP, chr, 1|0xC0000001)
            time.sleep(delay/10)
        x, y = GetCursorPos()
        PostMessage(hwnd, WM_KEYDOWN, 0x0D, 1|0x00000001)
        PostMessage(hwnd, WM_KEYUP, 0x0D, 1|0xC0000001)
        time.sleep(0.8)
        SetCursorPos((x, y))
        time.sleep(timeout/10)

    def setup_bp_windows(self):
        x = GetSystemMetrics(0) / 2
        y = GetSystemMetrics(1) / 2

        for winid in self.windows_found:
            window_hwnd_bot = str(winid).split(':', maxsplit=1)[0]
            #SetForegroundWindow(int(window_hwnd_bot))
            #SetFocus(int(window_hwnd_bot))
            mouse.move(int(x), int(y))
            ShowWindow(int(window_hwnd_bot), win32con.SW_MAXIMIZE)

    def miner(self, hwnd, dlugosc_stowniarek, szerokosc_stowniarek, okrazenia, bindy, delay, delay_mk):
        while self.kopacz_status == True:
            for i in range(okrazenia):
                if self.kopacz_status == False:
                    break
                mouse.press()
                keyboard.press('d')
                time.sleep(int(dlugosc_stowniarek)*0.22)
                keyboard.release('d')
                keyboard.press('w')
                time.sleep(int(szerokosc_stowniarek)*0.22)
                keyboard.release('w')
                keyboard.press('a')
                time.sleep(int(dlugosc_stowniarek)*0.22)
                keyboard.release('a')
                keyboard.press('s')
                time.sleep(int(szerokosc_stowniarek)*0.22)
                keyboard.release('s')
                self.okrazenia_done += 1
            if self.kopacz_status == False:
                break
            time.sleep(1)
            self.send_binds(bindy, delay_mk, delay)
    
    def miner_bg(self, nick, hwnd, dlugosc_stowniarek, szerokosc_stowniarek, bindy, delay, delay_mk):
        while self.kopacz_status == True:
            for i in range(99):
                print('11221')
                pass # TBD
    
    def miner_bg_bp(self, kontrola_zdalna, nick, hwnd, dlugosc_stowniarek, szerokosc_stowniarek, bindy, delay, delay_mk):
        global kopacz_status2
        time.sleep(1)
        okrazenia_zrobione = 0
        PostMessage(hwnd, 0x0007, 0, 0)
        win32gui.MoveWindow(hwnd, 100, -1000, 500, 500, True)
        while kopacz_status2 == True:
            if kopacz_status2 == False:
                break
            while self.kopacz_status_client == True:
                if kopacz_status2 == False:
                    break
                for i in range(999999999):
                    for index in bindy:
                        if (i % int(index[0])) == 0:
                            self.send_binds_bg_test(hwnd, index[1], delay_mk, delay)
                            pass
                    PostMessage(hwnd, WM_LBUTTONDOWN, 0x201, 1|0x00000001)
                    PostMessage(hwnd, WM_KEYDOWN, 0x44, 1|0x00000001)
                    time.sleep(int(dlugosc_stowniarek)*0.22)
                    PostMessage(hwnd, WM_KEYUP, 0x44, 1|0xC0000001)
                    PostMessage(hwnd, WM_KEYDOWN, 0x57, 1|0x00000001)
                    time.sleep(int(szerokosc_stowniarek)*0.22)
                    PostMessage(hwnd, WM_KEYUP, 0x57, 1|0xC0000001)
                    PostMessage(hwnd, WM_KEYDOWN, 0x41, 1|0x00000001)
                    time.sleep(int(dlugosc_stowniarek)*0.22)
                    PostMessage(hwnd, WM_KEYUP, 0x41, 1|0xC0000001)
                    PostMessage(hwnd, WM_KEYDOWN, 0x53, 1|0x00000001)
                    time.sleep(int(szerokosc_stowniarek)*0.22)
                    PostMessage(hwnd, WM_KEYUP, 0x53, 1|0xC0000001)
                    PostMessage(hwnd, WM_LBUTTONUP, 0x202, 1|0xC0000001)
                    self.kamien += dlugosc_stowniarek * szerokosc_stowniarek * 5
                    self.kratki += dlugosc_stowniarek * szerokosc_stowniarek
                    wk_thread = threading.Thread(target=self.send_miner_stats, args=('wykopany_kamien', (szerokosc_stowniarek*dlugosc_stowniarek*5), nick,), name='miner_wk_thread').start()
                    pk_thread = threading.Thread(target=self.send_miner_stats, args=('przebyte_kratki', (szerokosc_stowniarek*dlugosc_stowniarek), nick,), name='miner_pk_thread').start()
                    #zr_thread = threading.Thread(target=self.send_miner_stats, args=('zarobione_pieniadze', (self.pieniadze), nick,), name='miner_zp_thread').start()
                    if self.kopacz_status_client == False:
                        break
                    if kopacz_status2 == False:
                        break
                    #print(f'status miner: {kopacz_status2}')
            #print(f'waiting for miners... {kopacz_status2}')
            time.sleep(3)
        #print(f'ended {kopacz_status2}')
    def get_commands(self, bind):
        x = str(bind).split('*')
        x_to_return = []
        for i in x:
            if i == '':
                pass
            else:
                x_to_return.append(i)
        return x_to_return

    def execute_windows(self, hwnds):
        for hwnd in hwnds:
            hwnd_int = hwnd.split(':')[0]
            PostMessage(int(hwnd_int), WM_CLOSE,0,0)
        os._exit(0)

    def get_bot_activity(self, nick, okna):
        global kopacz_status2
        api = security.API()
        while kopacz_status2 == True:
            
            key = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for _ in range(12))
            response = api.get_bot_activities(nick, key)

            if response['status'] == 'success' and response['queue'] == 'start':
                self.kopacz_status_client = True
            elif response['status'] == 'success' and response['queue'] == 'stop':
                self.kopacz_status_client = False
            elif response['status'] == 'success' and response['queue'] == 'exit':
                self.kopacz_status_client = False
                self.execute_windows(okna)
            time.sleep(5)
            if kopacz_status2 == False:
                break

    def get_hwids(self, okna):
        hwids = []
        if type(okna) == list:
            for okno in okna:
                hwid = okno.split(' ')[0]
                hwids.append(hwid)
            return hwids
        hwids.append(okna.split(' ')[0])
        return hwids

    def start_bots(self,
                        nick,
                        okna,
                        dlugosc_stowniarek, 
                        szerokosc_stowniarek,
                        bindy,
                        delay,
                        delay_mk,
                        anty_rodzic_val,
                        anty_rodzic_godz,
                        tnt_logout,
                        folder_mc,
                        kopanie_w_tle,
                        kopanie_bp,
                        kontrola_zdalna):
        global kopacz_status2
        if kopacz_status2 == False:
            kopacz_status2 = True
            self.kopacz_status_client = True
            self.elapsed_time = time.time()
            hwids = []
            for hwid in okna:
                hwids.append(int(hwid.split(':')[0]))
            if kontrola_zdalna == True:
                threading.Thread(target=self.get_bot_activity, args=(nick,okna,)).start()
            api = security.API()
            key = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for _ in range(12))
            response11 = api.send_bot_activity(nick, key)
            if response11['status'] == 'success':
                if kopanie_w_tle == True:
                    if kopanie_bp == True:
                        for hwid in hwids:
                            threading.Thread(target=self.miner_bg_bp, args=(kontrola_zdalna, nick, hwid, dlugosc_stowniarek, szerokosc_stowniarek, bindy, delay, delay_mk,), name='miner_thread').start()
                    else:
                        threading.Thread(target=self.miner_bg, name='miner_thread').start()
                else:
                    threading.Thread(target=self.miner, name='miner_thread').start()
                if anty_rodzic_val == True:
                    threading.Thread(target=self.anty_rodzic, args=(anty_rodzic_godz,), name='miner_antyrodzic_thread').start()
                if tnt_logout == True:
                    threading.Thread(target=self.tnt_logout, args=(folder_mc,), name='miner_tnt_logout_thread').start()
        else:
            self.kopacz_status_client = True
        self.send_minecraft_ss()
