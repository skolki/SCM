import pyotp
import json
import base64
import binascii
import time
import pyautogui
import subprocess
from steam.guard import SteamAuthenticator
from colorama import init
init()
from colorama import Fore, Back, Style

print(Style.BRIGHT + '\n\n\n     SCM by @oskolkitg\n')
print('     Games list: Cats Banana Egg\n\n')
print(Fore.CYAN + '     TG софта: t.me/oskolkifarm\n')
print(Fore.GREEN + '     lolz.live/crydes\n')
print('     github.com/skolki\n\n\n')
time.sleep(2)




while True:

    # Функция для автоматического ввода текста
    def type_text(text):
        for char in text:
            pyautogui.press(char)
            time.sleep(0.02)  # задержка между нажатиями

    def get_steam_guard_code(mafile_path):
        """
        Get the Steam Guard code from a maFile.

        Args:
        mafile_path (str): The path to the maFile.

        Returns:
        str: The current Steam Guard code.
        """
        try:
            # Load the maFile
            with open(mafile_path, 'r') as file:
                mafile_data = json.load(file)

            # Create SteamAuthenticator instance
            authenticator = SteamAuthenticator(mafile_data)

            # Generate the Steam Guard code
            steam_guard_code = authenticator.get_code()
            return steam_guard_code
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


    # Функция для запуска игры через Steam
    def launch_game(steam_path, game_id, username, password, mafile_path):
        # Запуск Steam
        subprocess.Popen([steam_path])
        time.sleep(10)  # ожидание загрузки Steam

        # Добавить аккаунт
        pyautogui.click(x=1242, y=545)  # координаты кнопки плюс
        time.sleep(3) # Если есть выбор среди аккаунтов, ранее логинившихся "кто играет?". // Если нет - смело убирайте эту строчку.

        # Ввод логина
        pyautogui.click(x=692, y=440)  # координаты поля ввода логина
        type_text(username)

        # Ввод пароля
        pyautogui.click(x=670, y=525)  # координаты поля ввода пароля
        type_text(password)

        # Нажатие кнопки входа
        pyautogui.click(x=809, y=609)  # координаты кнопки входа
        time.sleep(2)  # ожидание входа в аккаунт

        # Генерация и ввод кода двухфакторной аутентификации
        auth_code = get_steam_guard_code(mafile_path)
        pyautogui.click(x=838, y=477)  # координаты поля ввода кода
        type_text(auth_code)
        time.sleep(7)

        # Cats
        subprocess.Popen([steam_path, f"steam://rungameid/{game_id}"])
        time.sleep(3)

        # Banana
        subprocess.Popen([steam_path, f"steam://rungameid/{game_id2}"])
        time.sleep(3)  # сколько сидеть в игре

        # Egg
        subprocess.Popen([steam_path, f"steam://rungameid/{game_id3}"])
        time.sleep(15)  # сколько сидеть в игре

        # Закрытие Cats
        subprocess.Popen('taskkill /im Cats.exe /f')
        time.sleep(2)
        # Закрытие Banana
        subprocess.Popen('taskkill /im Banana.exe /f')
        time.sleep(2)
        # Закрытие Egg
        subprocess.Popen('taskkill /im Egg.exe /f')
        time.sleep(2)
        # Закрытие Steam
        subprocess.Popen('taskkill /im steam.exe /f')
        time.sleep(2)
    # Основной код
    steam_path = 'C:/Steam/steam.exe'  # 123 путь к Steam
    game_id = '2977660'  # ID Cats
    game_id2 = '2923300'  # ID Banana
    game_id3 = '2784840' # ID Egg
    accounts = [
        {'username': '123', 'password': '123', 'mafile_path': 'C:/maFiles/123.maFile'},
        {'username': '123', 'password': '123', 'mafile_path': 'C:/maFiles/123.maFile'},
        {'username': '123', 'password': '123', 'mafile_path': 'C:/maFiles/123.maFile'},
    ]

    for account in accounts:
        launch_game(steam_path, game_id, account['username'], account['password'], account['mafile_path'])
        time.sleep(5)  # задержка между аккаунтами

    time.sleep(9800)
