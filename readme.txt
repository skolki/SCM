Script works as macros, so it can be problematic using PC during script execution
Your steam must not be running
And make sure you are using ENG keyboard layout

1. Install all of these

pip install pyotp
pip install pyautogui
pip install steam
pip install google
pip install --upgrade google-api-python-client
pip install subprocess
pip install winapi
pip install colorama

2. Open SCM.py in IDE
3. Use hotkey ctrl + f and find "123", change this data
4. Pixel positions can be wrong, you'll need to rewrite them
I used this software to get coords: https://github.com/ElektroStudios/Mouse-Point-Viewer/releases
5. Change time.sleep depending on your system

If you want collect Cats by its timer, change this time.sleep to 90+
time.sleep(15)  # сколько сидеть в игре

Script stops by ctrl + c
