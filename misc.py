from httpcore import TimeoutException
import requests, threading, json, webbrowser, re, time, codecs, os, security
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from multiprocessing.pool import ThreadPool
from random import randint
from time import sleep, strftime

def check_for_existing_threads(thread_name):
    while True:
        time.sleep(1)
        going_threads = []
        for thread in threading.enumerate():
            if thread_name in thread.name:
                going_threads.append(thread.name)
        if len(going_threads) == 0:
            return True

def createdirectory(p, name):
    today = f'{strftime(f"%d.%m.%H;%M")}'
    try:
        directory = ""
        directory2 = f"results/{p}"
        pathf = f"{name}-{str(today)}"
        path = os.path.join(directory, directory2)
        mode = 0o666
        os.mkdir(path, mode)
        sleep(1)
    except:
        pass
    try:
        path1 = os.path.join(directory2, pathf)
        mode = 0o666
        os.mkdir(path1, mode)
    except Exception as e:
        pass
    return pathf

def odczyt_pliku(filename,method):
    try:
        with open(filename,method, encoding='utf-8', errors='ignore') as f:
            content = [line.strip('\n') for line in f]
            f.close()
            return content
    except:
        pass


####################################################
#                     DISCORD                      #
####################################################

def discord_server():
    webbrowser.open('https://discord.gg/sW5TmXPH74', new=2)