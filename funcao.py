import datetime

import pyautogui                                                        # Import pyautogui.
from datetime import date
import time
import pyscreenshot as ImageGrab


def main():                                                             # Main function.
    opensafari()                                                        # Call openChrome.
    openwebsites('www.mercadolivre.com.br')                             # Call open websites with the websites.
    time.sleep(10)
    acessarvendas()
    printsituacao()
    enviosituacao()


def opensafari():                                                       # Função para abrir o safari no macOS.
    pyautogui.click(x=153, y=862)                                       # clica no icone do safari
    time.sleep(3)
    pyautogui.click(x=129, y=51)                                        # aumenta a janela
    time.sleep(3)
    pyautogui.click(x=1374, y=25)                                       # abre uma nova aba


def openwebsites(url):                                                 # Funcao que abre o website do mercado Livre
    pyautogui.typewrite(url, interval=0.001)                           # Write the website with a 0.001 delay.
    pyautogui.typewrite(['enter'])                                     # Press enter.


def acessarvendas():                                                    # função para acessar a aba 'vendas'
    pyautogui.moveTo(x=1036, y=159)                                     # clica no nome de usuario
    time.sleep(1)
    pyautogui.click(x=920, y=677)                                       # clica na opção 'vendas


def printsituacao():
    time.sleep(4)
    im = ImageGrab.grab()
    im.save("situaçãovendas.png")
    time.sleep(2)


def enviosituacao():
    time.sleep(2)
    pyautogui.click(x=1374, y=25)
    emailurl = 'www.outlook.com'
    pyautogui.typewrite(emailurl, interval=0.001)
    pyautogui.typewrite(['enter'])
    time.sleep(5)
    pyautogui.click(x=209, y=146)
    time.sleep(5)
    email = 'jeancarlossilva2015@hotmail.com'
    pyautogui.typewrite(email, interval=0.002)
    pyautogui.typewrite(['enter'])
    time.sleep(1)
    pyautogui.typewrite(['tab'])
    time.sleep(1)
    pyautogui.typewrite(f' RESUMO DAS VENDAS PLAT: MERCADO LIVRE - DATA:  {datetime.date.today()}',  interval=0.002)
    time.sleep(1)
    pyautogui.click(x=888, y=640)
    time.sleep(1)
    pyautogui.click(x=968, y=536)
    time.sleep(2)
    pyautogui.click(x=942, y=235)
    pyautogui.typewrite('SituacaoVendas', interval=0.001)
    time.sleep(1)
    pyautogui.click(x=595, y=285)
    time.sleep(1)
    pyautogui.click(x=797, y=375)
    # pyautogui.click(x=1016, y=685)











