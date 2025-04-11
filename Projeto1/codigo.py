import pyautogui        #realizar automações c/ mouse e teclado
import time             #realizar controle de tempo
import pandas           #realizar manipulação de dados

# Passo 1: Entrar no sistema da empresa
pyautogui.PAUSE = 0.5

# abriBOHA000251    r o firefox mozilla
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

# Passo 5: Repetir para todos os produtos - passo 4 dentro de um for
for linha in tabela.index:                         #p/ cada linha da tabela
    pyautogui.click(x=1964, y=372)

    codigo = tabela.loc[linha, "codigo"]           #loc = localizar uma informação na linha e coluna
    pyautogui.write(codigo)

    pyautogui.press("tab")      
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])         #converter nº p/ string
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":            #nan -> Not a Number
        pyautogui.write(obs)

    pyautogui.press("tag")      
    pyautogui.press("enter")    

    pyautogui.scroll(10000)     
