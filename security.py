import requests, psutil, subprocess, base64, time, random, ast, json, threading, os
from datetime import date
from textwrap import wrap

debugger_names = ["NETSTAT","FILEMON","PROCMON","REGMON","CAIN","NETMON","Tcpview","vpcmap","vmsrvc","vmusrvc","wireshark","VBoxTray","VBoxService","IDA","WPE PRO","The Wireshark Network Analyzer","WinDbg","OllyDbg","Colasoft Capsa","Microsoft Network Monitor","Fiddler","SmartSniff","Immunity Debugger","Process Explorer","PE Tools","AQtime","DS-5 Debug","Dbxtool","Topaz","FusionDebug","NetBeans","Rational Purify",".NET Reflector","Cheat Engine","Sigma Engine","codecracker","x32dbg","x64dbg","ida","charles","dnspy","simpleassembly","peek","httpanalyzer","httpdebug","fiddler","wireshark","proxifier","mitmproxy","ethereal","airsnare","smsniff","smartsniff","netmon","processhacker","killswitch","codecracker","ghidra","Burpsuite","Ghidra","dnSpy","Fiddler","HxD","ILSpy","dumpcap","HTTPDebugger"]

def security_thread():
    for proc in psutil.process_iter():
        try:
            for debugger in debugger_names:
                if debugger.lower() in proc.name().lower():
                    #sys.exit()
                    #os._exit(0)
                    pass
                    #return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def check_for_debuggers():
    while True:
        for proc in psutil.process_iter():
            for debugger in debugger_names:
                if debugger.lower() in proc.name().lower():
                    #os._exit(0)
                    pass
        time.sleep(5)

def count_online_users():
    api = API()
    key = ''.join(random.choice('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890') for _ in range(12))
    response = api.get_online(key)

def debug_start():
    threading.Thread(target=check_for_debuggers).start()

class CRYPT(object):
    chars = ['q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T',
        'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P',
        'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G',
        'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z',
        'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N',
        'm', 'M', '1', '!', '2', '@', '3', '#', '4', '$',
        '5', '%', '6', '^', '7', '&', '8', '*', '9', '0',
        '-', '_', '=', '+', '{', '}', '[', ']', '\\', '"',
        ';', ':', ',', '.', '<', '>', '/', '?', '`', '~', ' ', '|']
    
    list_of_chars = {
        'q':'QA>A', 'Q':'Z`Tn', 'w':'v#ZA', 'W':'DJo1', 'e':'$q%n', 'E':'-epe',
        'r':'s\oz', 'R':'&Jqb', 't':'"#`c', 'T':'W9@C', 'y':'%NTv', 'Y':'S53]',
        'u':'R>$3', 'U':'kb"!', 'i':',8QN', 'I':'<;P}', 'o':'5e0L', 'O':'VbtT',
        'p':'nk8}', 'P':'=OqJ', 'a':'tlWL', 'A':'L!,A', 's':'x_B+', 'S':'"bC[',
        'd':'D}a"', 'D':'R$Sx', 'f':'9mLR', 'F':'!si4', 'g':'DA1k', 'G':'PP7-',
        'h':'Q2Zl', 'H':'lrTt', 'j':'=2"k', 'J':'%3H2', 'k':'jDP^', 'K':'"^SQ',
        'l':'qN6F', 'L':'$;Dr', 'z':'15~c', 'Z':'TYsB', 'x':'b{#p', 'X':'[$P9',
        'c':'5EXq', 'C':'&D&4', 'v':'gE@^', 'V':'2Ck2', 'b':'0~Ps', 'B':'#8*v',
        'n':'gf&;', 'N':'M\K]', 'm':'H4B6', 'M':'l\A!', '1':'sF_i', '!':'fZti',
        '2':'7<oZ', '@':'yzfM', '3':'R>f&', '#':'*UU8', '4':'R7Vs', '$':'kyP"',
        '5':'Gv>&', '%':'i!H$', '6':'klz-', '^':'4*qx', '7':'~216', '&':'b>?8',
        '8':'%}7O', '*':'%Sj{', '9':'ud:8', '0':'`8Q4', '-':'^3Tm', '_':'X+"5',
        '=':'>/H+', '+':'8{\s', '{':'~Go6', '}':'kgb5', '[':'oL%T', ']':'fn\e',
        '\\':'wttu', '"':'?,nE', ';':'r^Aw', ':':'1sS*', ',':'z<b[', '.':'EXTU',
        '<':'&2Qa', '>':'#]%k', '/':'^g,z', '?':'2!6Y', '`':'6dIV', '~':'8{Yz',
        ' ':'BhaQ', '|':'PPKA'}
    
    def get_text_elements(self, text):
        text_chars = []
        for x in range(len(text)):
            text_chars.append(text[x])
        return text_chars

    def key_generator(self, text):
        te = self.get_text_elements(text)
        key = ''
        for x in range(len(te)):
            index = self.chars.index(te[x])
            fixed_value = len(self.chars) - 1 - index
            if fixed_value > 9:
                random_int = random.randint(1,9)
            else:
                random_int = random.randint(1, fixed_value)
            key += str(random_int)
        return str(key)

    def modify_chars(self, mode, text, key):
        data = ''
        if mode == 'decode':
            key_splitted = self.get_text_elements(str(key))
            text_len = len(text)
            for x in range(text_len):
                index = self.chars.index(text[x])
                data += self.chars[index-int(key_splitted[x])]
            return data
        elif mode == 'encode':
            key_splitted = self.get_text_elements(str(key))
            text_len = len(text)
            for x in range(text_len):
                index = self.chars.index(text[x])
                data += self.chars[index+int(key_splitted[x])]
            return data

    def decode(self, text):
        data = ''
        decoded = base64.b64decode(text).decode()
        key = decoded.split('.')[0]
        decoded = decoded.split('.')[1]
        crypt = wrap(decoded, 4)
        for x in range(len(crypt)):
            for value in self.list_of_chars:
                if crypt[x] == self.list_of_chars[value]:
                    data += value
        message = self.modify_chars('decode', data, str(key))
        return message

    def encode(self, text):
        key = self.key_generator(text)
        data = f'{key}.'
        message = self.modify_chars('encode', text, str(key))
        for x in range(len(message)):
            data += self.list_of_chars[message[x]]
        encoded = base64.b64encode(data.encode('utf-8')).decode()
        return encoded

class API(object):
    def get_server_status(self, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"status",
                "key":key
            }
            response = requests.post('https://pvpbooster.pl/api2/connection', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def return_top_data(self, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"return_top_data",
                "key":key
                }
            response = requests.post('https://pvpbooster.pl/api2/statystyki', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                return ast.literal_eval(response_decoded)
            return False
        except:
            return False
        
    def create_user_stats(self, username, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"create_stats",
                "nickname":username,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/statystyki', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def get_bot_activities(self, username, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"get_activities",
                "nickname":username,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/miner', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def update_bot_activities(self, activity, username, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"send_activities",
                "nickname":username,
                "activity":activity,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/miner', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def send_bot_activity(self, username, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"send_activities",
                "activity":"insert",
                "nickname":username,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/miner', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def delete_bot_activity(self, username, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"send_activities",
                "nickname":username,
                "activity":'delete',
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/miner', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def send_stats(self, stats, value, username, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"update_stats",
                "stats":stats,
                "value":value,
                "nickname":username,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/statystyki', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def get_user_discord_id(self, username, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"get_id",
                "nickname":username,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/dc_user', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def set_user_discord_id(self, username, discord_id, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"insert_user",
                "nickname":username,
                "discord_id":discord_id,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/dc_user', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def update_hwid(self, username, hwid, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"update_hwid",
                "nickname":username,
                "hwid":hwid,
                "key":key
                }
            response = requests.post(f'https://pvpbooster.pl/api2/login', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def login(self, username, password, hwid, key):
        crypt = CRYPT()
        try:
            data = {'mode':'check_data',
                    'nickname':username,
                    'password':password,
                    'hwid':hwid,
                    'key':key}
            response = requests.post(f'https://pvpbooster.pl/api2/login', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def register(self, email, username, password, key, key2):
        crypt = CRYPT()
        try:
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            date_now = date.today()
            personal_id = random.randint(10000, 99999)
            data = {
                "mode":"add_user",
                "personal_id":personal_id,
                "email":email,
                "nickname":username,
                "password":password,
                "hwid":hwid,
                "hwid_status":"filled",
                "license_key":key,
                "registration_date":date_now,
                "key":key2
            }
            response = requests.post(f'https://pvpbooster.pl/api2/signup', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def get_online(self, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"get",
                "key":key
            }
            response = requests.post('https://pvpbooster.pl/api2/online', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False

    def set_online(self, nickname, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"add",
                "nickname":nickname,
                "key":key
            }
            response = requests.post(f'https://pvpbooster.pl/api2/online', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False
    
    def delete_online(self, nickname, key):
        crypt = CRYPT()
        try:
            data = {
                "mode":"delete",
                "nickname":nickname,
                "key":key
            }
            response = requests.post(f'https://pvpbooster.pl/api2/online', data=data).text
            if response != '':
                response_decoded = crypt.decode(response)
                response_json = json.loads(response_decoded)
                return response_json
            return False
        except:
            return False
    
    def login(self, username, password, hwid, key):
        if self.get_server_status(key) == True:
            data = {'mode':'check_data',
                    'nickname':username,
                    'password':password,
                    'hwid':hwid,
                    'key':key}
            response = requests.post(f'http://srv46163.seohost.com.pl/api/login.php', data=data).text
            return response
        return 'error'

    def register(self, email, username, password, key, key2):
        crypt = CRYPT()
        if self.get_server_status(key) == True:
            hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
            date_now = date.today()
            personal_id = random.randint(10000, 99999)
            data = {
                "mode":"add_user",
                "personal_id":personal_id,
                "email":email,
                "nickname":username,
                "password":password,
                "hwid":hwid,
                "hwid_status":"filled",
                "license_key":key,
                "registration_date":date_now,
                "key":key2
            }
            response = requests.post(f'http://srv46163.seohost.com.pl/api/signup.php', data=data).text
            return response
        return 'error'