import random as rd
import pyautogui as auto
import string
from time import sleep

def cria_blocotexto(lista: list, nome: str or None=None):
    nome_aleatorio = ''.join(rd.choice(string.ascii_lowercase) for _ in range(10)) if nome==None else nome

    auto.press("win")
    auto.write("Notepad")
    auto.press("enter")

    sleep(2)
    for item in lista:
        tempo_var= rd.randint(1, 3)/rd.randint(4, 10)
        auto.write(item, interval=tempo_var)
        auto.press("enter")

    auto.hotkey("ctrl", "s")
    auto.write(f"{nome_aleatorio}.txt")
    auto.press("enter")
    auto.hotkey("alt", "f4")

list_teste =  ["Apple", "Banana", "Abacaxi"]       
cria_blocotexto(lista=list_teste, nome="rwqr")