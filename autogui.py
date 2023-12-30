import pyautogui as pag
import time
from scrape_letters import scrape
from words import valid_words

def autogui(words):
    pag.hotkey('command', 'tab', interval=0.25)

    for word in words:
        pag.write(word)
        time.sleep(0.25)
        pag.press('enter')
        time.sleep(0.25)



if __name__ == '__main__':
    letters = scrape()
    words = valid_words(letters)
    autogui(words)