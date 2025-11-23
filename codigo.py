# ------------------------- IMPORTS DE BIBLIOTECAS -------------------------
import pyautogui
import time
import pandas as pd

# ------------------------- CONFIGURAÇÃO INICIAL -------------------------
# Pausa de 0.5 segundos entre cada comando do pyautogui
pyautogui.PAUSE = 0.5

# --------------------------------------------------------------------------
# PASSO 1: ABRIR O NAVEGADOR E ACESSAR O SITE
# --------------------------------------------------------------------------
# Apertar a tecla do Windows
pyautogui.press("win")
# Escrever o nome do navegador
pyautogui.write("brave")
# Apertar Enter para abrir
pyautogui.press("enter")

# Aguardar 2 segundos para o navegador abrir
time.sleep(2)

# Digitar a URL do site e pressionar Enter
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Aguardar 3 segundos para a página carregar
time.sleep(3)

# --------------------------------------------------------------------------
# PASSO 2: FAZER LOGIN NO SISTEMA
# --------------------------------------------------------------------------
# Clicar no campo de e-mail (ajuste as coordenadas se necessário)
pyautogui.click(x=982, y=456)  # Lembre-se de ajustar esta coordenada, caso necessário!
pyautogui.write("Glauco_teste@gmail.com")

# Pressionar Tab para passar para o campo de senha
pyautogui.press("tab")
pyautogui.write("123456")

# Pressionar Tab para focar no botão de login e depois Enter
pyautogui.press("tab")
pyautogui.press("enter")

# Aguardar 3 segundos para a página de produtos carregar
time.sleep(3)

# --------------------------------------------------------------------------
# PASSO 3: IMPORTAR A BASE DE DADOS DE PRODUTOS
# --------------------------------------------------------------------------
tabela = pd.read_csv("produtos.csv")
print(tabela)

# --------------------------------------------------------------------------
# PASSO 4: CADASTRAR TODOS OS PRODUTOS
# --------------------------------------------------------------------------
# Loop para percorrer cada linha da tabela
for linha in tabela.index:
    # Clica no primeiro campo do formulário para garantir o foco
    pyautogui.click(x=615, y=313) # Lembre-se de ajustar esta coordenada!

    # Preencher os campos do formulário
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # <-- CORRIGIDO AQUI
    pyautogui.press("tab")

    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario)) # <-- CORRIGIDO AQUI
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo)) # <-- CORRIGIDO AQUI
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    # Verifica se a observação não é um valor nulo (NaN) antes de escrever
    if not pd.isna(obs):
        pyautogui.write(str(obs)) # <-- CORRIGIDO AQUI
    
    pyautogui.press("tab")

    # Pressionar Enter para enviar o formulário e cadastrar o produto
    pyautogui.press("enter")

    # Rolar a tela para cima para preparar para o próximo item
    pyautogui.scroll(5000)