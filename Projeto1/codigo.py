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
pyautogui.press("tab")      #passar p/ o próximo campo
pyautogui.write("minhaSenhaSuperSecreta")

# botão logar
pyautogui.press("tab")
#pyautogui.click(x=2316, y=717) 
pyautogui.press("enter")

# Passo 3: Importar a base de dados com pandas
tabela = pandas.read_csv("Projeto1/produtos.csv")

print(tabela)

 # Passo 4: Cadastrar 1º produto manualmente, depois automatiza o restante do processo
pyautogui.click(x=1964, y=372)

codigo = "MOLO000251"
pyautogui.write(codigo)

pyautogui.press("tab")      #passar p/ o próximo campo
marca = "Logitech"
pyautogui.write(marca)

pyautogui.press("tab")
tipo = "Mouse"
pyautogui.write(tipo)

pyautogui.press("tab")
categoria = "1"
pyautogui.write(categoria)

pyautogui.press("tab")
preco_unitario = "25.95"
pyautogui.write(preco_unitario)

pyautogui.press("tab")
custo = "6.50"
pyautogui.write(custo)

pyautogui.press("tab")
obs = ""
pyautogui.write("")

pyautogui.press("tag")      #passar p/ o botão logar
pyautogui.press("enter")    #enviar formulário

pyautogui.scroll(10000)     #nº positivo a rolagem vai para cima e negativo vai para baixo
                            #no lugar de nº, poderia usar teclas: home p/ cima e end p/ baixo

