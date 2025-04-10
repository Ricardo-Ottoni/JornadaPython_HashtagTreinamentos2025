import pyautogui        #realizar automações c/ mouse e teclado
import time             #realizar controle de tempo
import pandas           #realizar manipulação de dados

# Passo 1: Entrar no sistema da empresa
pyautogui.PAUSE = 0.5

# abrir o firefox mozilla
pyautogui.press("win")          #"press": apertar 1 tecla
pyautogui.write("firefox")      #"write": escrever 1 texto
pyautogui.press("enter")
time.sleep(3)

# digitar o site
pyautogui.click(x=1665, y=77)       #"click": clicar em algum lugar
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2: Fazer login
# campo email
time.sleep(3)
pyautogui.click(x=1964, y=513) 
pyautogui.write("meu_email_testando@.com")

# campo senha
pyautogui.press("tab")
pyautogui.write("minhaSenhaSuperSecreta")

# botão logar
pyautogui.press("tab")
#pyautogui.click(x=2316, y=717) 
pyautogui.press("enter")

# Passo 3: Importar a base de dados com pandas
tabela = pandas.read_csv("Projeto1/produtos.csv")

print(tabela)