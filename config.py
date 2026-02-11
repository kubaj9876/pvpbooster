import configparser, requests, os

config = configparser.ConfigParser()

def create_config(name):
    config['clicker'] = {'clicker_bind_clicker': 'x1button',
                     'clicker_bind_fakelag': 'z',
                     'clicker_bind_komenda': 'v',
                     'clicker_bind_sniezka': 'x2button',
                     'clicker_bind_zmiana_seta': 'b',
                     'clicker_sloty_miecz': '1',
                     'clicker_sloty_sniezka': '2',
                     'clicker_opcje_ms': '80',
                     'clicker_opcje_garda': 'False',
                     'clicker_opcje_garda_ms': '500',
                     'clicker_opcje_fakelag': 'False',
                     'clicker_opcje_fakelag_moc': '10',
                     'clicker_opcje_zmiana_seta': 'False',
                     'clicker_opcje_zmiana_seta_predkosc': '60',
                     'clicker_opcje_zmiana_seta_pozycje': '[1, 2, 3, 4]',
                     'clicker_opcje_komenda': 'True',
                     'clicker_opcje_komenda_text': '/schowek',
                     'clicker_opcje_sniezka': 'False',
                     'clicker_opcje_jitter': 'False'}
                     #'clicker_opcje_podglad': 'True',
                     #'clicker_opcje_aim_assist': 'False'}
    config['miner'] = {'miner_ustawienia_dlugosc_stowniarek': '10',
                     'miner_ustawienia_szerokosc_stowniarek': '2',
                     'miner_ustawienia_wpisywanie_komendy': '0.6',
                     'miner_ustawienia_czas_m_komendami': '0.6',
                     'miner_komendy_lista': '["/repair [10]", "/sellall [30]"]',
                     'miner_opcje_anty_rodzic': 'False',
                     'miner_opcje_anty_rodzic_godzina': '01:03',
                     'miner_opcje_tnt_logout': 'False',
                     'miner_opcje_tnt_logout_sciezka': 'C:\\Users\\Test\\AppData\\Roaming\\.minecraft',
                     'miner_opcje_kopanie_w_tle': '2',
                     'miner_opcje_kopanie_w_tle_bp': '2',
                     'miner_opcje_auto_rejoin': 'False',
                     'miner_opcje_kontrola_zdalna': 'False'}
    config['premium'] = {'premium_passhunter_threads': '10',
                     'premium_dehasher_threads': '10',
                     'premium_keyword_scraper_threads': '10'}

    with open(f"{name}.ini", "w") as f:
        config.write(f)

def load_config(name):
    config.read(f"{name}.ini")

    clicker_bind_clicker = str(config.get("clicker", "clicker_bind_clicker"))
    clicker_bind_fakelag = str(config.get("clicker", "clicker_bind_fakelag"))
    clicker_bind_komenda = str(config.get("clicker", "clicker_bind_komenda"))
    clicker_bind_sniezka = str(config.get("clicker", "clicker_bind_sniezka"))
    clicker_bind_zmiana_seta = str(config.get("clicker", "clicker_bind_zmiana_seta"))
    clicker_sloty_miecz = str(config.get("clicker", "clicker_sloty_miecz"))
    clicker_sloty_sniezka = str(config.get("clicker", "clicker_sloty_sniezka"))
    clicker_opcje_clicker_ms = int(config.get("clicker", "clicker_opcje_ms"))
    clicker_opcje_clicker_garda = bool(config.get("clicker", "clicker_opcje_garda"))
    clicker_opcje_clicker_garda_ms = int(config.get("clicker", "clicker_opcje_garda_ms"))
    clicker_opcje_clicker_fakelag = bool(config.get("clicker", "clicker_opcje_fakelag"))
    clicker_opcje_clicker_fakelag_moc = int(config.get("clicker", "clicker_opcje_fakelag_moc"))
    clicker_opcje_clicker_zmiana_seta = bool(config.get("clicker", "clicker_opcje_zmiana_seta"))
    clicker_opcje_clicker_zmiana_seta_pozycje = list(config.get("clicker", "clicker_opcje_zmiana_seta_pozycje"))
    clicker_opcje_clicker_zmiana_seta_predkosc = int(config.get("clicker", "clicker_opcje_zmiana_seta_predkosc"))
    clicker_opcje_komenda = bool(config.get("clicker", "clicker_opcje_komenda"))
    clicker_opcje_komenda_text = str(config.get("clicker", "clicker_opcje_komenda_text"))
    clicker_opcje_sniezka = bool(config.get("clicker", "clicker_opcje_sniezka"))
    clicker_opcje_jitter = bool(config.get("clicker", "clicker_opcje_jitter"))
    #clicker_opcje_aim_assist = bool(config.get("clicker", "clicker_opcje_aim_assist"))
    
    miner_ustawienia_dlugosc_stowniarek = int(config.get("miner", "miner_ustawienia_dlugosc_stowniarek"))
    miner_ustawienia_szerokosc_stowniarek = int(config.get("miner", "miner_ustawienia_szerokosc_stowniarek"))
    miner_ustawienia_wpisywanie_komendy = float(config.get("miner", "miner_ustawienia_wpisywanie_komendy"))
    miner_ustawienia_czas_m_komendami = float(config.get("miner", "miner_ustawienia_czas_m_komendami"))
    miner_komendy_lista = list(config.get("miner", "miner_komendy_lista"))
    miner_opcje_anty_rodzic = bool(config.get("miner", "miner_opcje_anty_rodzic"))
    miner_opcje_anty_rodzic_godzina = str(config.get("miner", "miner_opcje_anty_rodzic_godzina"))
    miner_opcje_tnt_logout = bool(config.get("miner", "miner_opcje_tnt_logout"))
    miner_opcje_tnt_logout_sciezka = str(config.get("miner", "miner_opcje_tnt_logout_sciezka"))
    miner_opcje_kopanie_w_tle = bool(config.get("miner", "miner_opcje_kopanie_w_tle"))
    miner_opcje_kopanie_w_tle_bp = bool(config.get("miner", "miner_opcje_kopanie_w_tle_bp"))
    miner_opcje_auto_rejoin = bool(config.get("miner", "miner_opcje_auto_rejoin"))
    miner_opcje_kontrola_zdalna = bool(config.get("miner", "miner_opcje_kontrola_zdalna"))
    
    premium_passhunter_threads = int(config.get("premium", "premium_passhunter_threads"))
    premium_dehasher_threads = int(config.get("premium", "premium_dehasher_threads"))
    premium_keyword_scraper_threads = int(config.get("premium", "premium_keyword_scraper_threads"))
    
    return [clicker_bind_clicker, clicker_bind_fakelag, clicker_bind_komenda, clicker_bind_sniezka, clicker_bind_zmiana_seta, clicker_sloty_miecz, clicker_sloty_sniezka, clicker_opcje_clicker_ms, clicker_opcje_clicker_garda, clicker_opcje_clicker_garda_ms, clicker_opcje_clicker_fakelag, clicker_opcje_clicker_fakelag_moc, clicker_opcje_clicker_zmiana_seta, clicker_opcje_clicker_zmiana_seta_predkosc, clicker_opcje_clicker_zmiana_seta_pozycje, clicker_opcje_komenda, clicker_opcje_komenda_text, clicker_opcje_sniezka, clicker_opcje_jitter, miner_ustawienia_dlugosc_stowniarek, miner_ustawienia_szerokosc_stowniarek, miner_ustawienia_wpisywanie_komendy, miner_ustawienia_czas_m_komendami, miner_komendy_lista, miner_opcje_anty_rodzic, miner_opcje_anty_rodzic_godzina, miner_opcje_tnt_logout, miner_opcje_tnt_logout_sciezka, miner_opcje_kopanie_w_tle, miner_opcje_kopanie_w_tle_bp, miner_opcje_auto_rejoin, miner_opcje_kontrola_zdalna, premium_passhunter_threads, premium_dehasher_threads, premium_keyword_scraper_threads]

def save_config(values, name):
    config.read(f"{name}.ini")
    
    config.set('clicker', 'clicker_bind_clicker', str(values[0]))
    config.set('clicker', 'clicker_bind_fakelag', str(values[1]))
    config.set('clicker', 'clicker_bind_komenda', str(values[2]))
    config.set('clicker', 'clicker_bind_sniezka', str(values[3]))
    config.set('clicker', 'clicker_bind_zmiana_seta', str(values[4]))
    config.set('clicker', 'clicker_sloty_miecz', str(values[5]))
    config.set('clicker', 'clicker_sloty_sniezka', str(values[6]))
    config.set('clicker', 'clicker_opcje_ms', str(values[7]))
    config.set('clicker', 'clicker_opcje_garda', str(values[8]))
    config.set('clicker', 'clicker_opcje_garda_ms', str(values[9]))
    config.set('clicker', 'clicker_opcje_fakelag', str(values[10]))
    config.set('clicker', 'clicker_opcje_fakelag_moc', str(values[11]))
    config.set('clicker', 'clicker_opcje_zmiana_seta', str(values[12]))
    config.set('clicker', 'clicker_opcje_zmiana_seta_predkosc', str(values[13]))
    config.set('clicker', 'clicker_opcje_zmiana_seta_pozycje', str(values[14]))
    config.set('clicker', 'clicker_opcje_komenda', str(values[15]))
    config.set('clicker', 'clicker_opcje_komenda_text', str(values[16]))
    config.set('clicker', 'clicker_opcje_sniezka', str(values[17]))
    config.set('clicker', 'clicker_opcje_jitter', str(values[18]))
    #config.set('clicker', 'clicker_opcje_aim_assist', str(values[20]))
    
    config.set('miner', 'miner_ustawienia_dlugosc_stowniarek', str(values[19]))
    config.set('miner', 'miner_ustawienia_szerokosc_stowniarek', str(values[20]))
    config.set('miner', 'miner_ustawienia_wpisywanie_komendy', str(values[21]))
    config.set('miner', 'miner_ustawienia_czas_m_komendami', str(values[22]))
    config.set('miner', 'miner_komendy_lista', str(values[23]))
    config.set('miner', 'miner_opcje_anty_rodzic', str(values[24]))
    config.set('miner', 'miner_opcje_anty_rodzic_godzina', str(values[25]))
    config.set('miner', 'miner_opcje_tnt_logout', str(values[26]))
    config.set('miner', 'miner_opcje_tnt_logout_sciezka', str(values[27]))
    config.set('miner', 'miner_opcje_kopanie_w_tle', str(values[28]))
    config.set('miner', 'miner_opcje_kopanie_w_tle_bp', str(values[29]))
    config.set('miner', 'miner_opcje_auto_rejoin', str(values[30]))
    config.set('miner', 'miner_opcje_kontrola_zdalna', str(values[31]))
    
    config.set('premium', 'premium_passhunter_threads', str(values[32]))
    config.set('premium', 'premium_dehasher_threads', str(values[33]))
    config.set('premium', 'premium_keyword_scraper_threads', str(values[34]))
    
    with open(f"{name}.ini", "w") as f:
        config.write(f)
        
def generate_base64(values):
    if len(values) > 0:
        data = {'input': f'{values}',
                'charset': 'UTF-8',
                'separator': 'crlf'}
        try:
            req = requests.post('https://www.base64encode.org', data=data).text
            response = req.split('"Result goes here..." spellcheck="false">')
            x = str(str(str(response[1].split('</textarea>')[0]).replace('&#039;', '')).removeprefix('[').removesuffix(']')).split(', ')[0]
            return x
        except:
            return 'error'
    else:
        return 'error'

def load_base64(values):
    if len(values) > 0:
        data = {"input":f"{values}",
              "charset": "UTF-8"}

        try:
            req = requests.post('https://www.base64decode.org', data=data).text
            response = req.split('"Result goes here..." spellcheck="false">')
            x = str(str(str(response[1].split('</textarea>')[0]).replace('&#039;', '')).removeprefix('[').removesuffix(']')).split(', ')
            return x
        except:
            return 'error'
    else:
        return 'error'