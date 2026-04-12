# 1° Abrir o chrome
# 2° Abrir o sistema
# 3° Fazer login no sistema
# 4° Abrir a base de dados
# 5° Cadastrar todos os produtos da tabela

import pyautogui
import time
import pandas

pyautogui.PAUSE = 2

# 1° Abrir o chrome
pyautogui.press("win")
pyautogui.press("enter")
pyautogui.press("enter")
time.sleep(4)

# 2° Abrir o sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # Fictício
pyautogui.press("enter")

# 3° Fazer login no sistema
pyautogui.press("tab")
pyautogui.write("aleatorio@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(4)

# 4° Abrir a base de dados
tabela = pandas.read_csv("produtos.csv")

# 5° Cadastrar todos os produtos da tabela
for linha in tabela.index:
    pyautogui.click(x=516, y=260)
    
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(5000)