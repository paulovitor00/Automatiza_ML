import pyautogui                                                        # Import pyautogui.
import time


def main():                                                             # Main function.
    openSafari()                                                        # Call openChrome.
    openWebsites('www.mercadolivre.com.br')                             # Call open websites with the websites.
    time.sleep(10)
    acessarVendas()


def openSafari():                                                       # Function to open chrome.
    pyautogui.click(x=153, y=862)                                       #clica no icone do safari
    time.sleep(3)
    pyautogui.click(x=129, y=51)                                        #aumenta a janela
    time.sleep(3)
    pyautogui.click(x=1374, y=25)                                       #abre uma nova aba


def openWebsites(url):                                                 # Funcao que abre o website
        pyautogui.typewrite(url, interval=0.001)                       # Write the website with a 0.001 delay.
        pyautogui.typewrite(['enter'])                                 # Press enter.


def acessarVendas():
    pyautogui.moveTo(x=1036, y=159)                 #clica no nome de usuario
    time.sleep(1)
    pyautogui.click(x=920, y=677)                   #clica na opção vendas


