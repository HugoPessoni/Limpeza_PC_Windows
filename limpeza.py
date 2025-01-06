import pyautogui
import time
import sys

def limpar_temp_2(deve_acontecer_temp_2):
    """
    Função para limpar a pasta %temp% no Windows.
    """

    deve_acontecer = deve_acontecer_temp_2

    if not deve_acontecer:
        print("Pasta '%Temp%' desativada")
        return

    try:
        # Passo 2: Pressionar Win + R
        pyautogui.hotkey('win', 'r')
        time.sleep(2) 

        # Passo 3: Digitar 'recent'
        pyautogui.typewrite('%temp%', interval=0.05)
        time.sleep(2)

        # Passo 4: Pressionar Enter
        pyautogui.press('enter')
        time.sleep(3)  

        # Passo 5: Clicar nos arquivos
        # Substitua X_ARQUIVOS e Y_ARQUIVOS pelas coordenadas corretas do seu computador
        X_ARQUIVOS = 1547  
        Y_ARQUIVOS = 276 
        pyautogui.click(X_ARQUIVOS, Y_ARQUIVOS)
        time.sleep(2)

        # Passo 6: Selecionar todos os itens com Ctrl + A
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)

        # Passo 7: Pressionar Delete
        pyautogui.press('delete')
        time.sleep(10)

        # Passo 8: Clicar em continuar
        # Substitua X_ARQUIVOS e Y_ARQUIVOS pelas coordenadas corretas do seu computador
        X_ARQUIVOS = 895  
        Y_ARQUIVOS = 472
        pyautogui.click(X_ARQUIVOS, Y_ARQUIVOS)
        time.sleep(2)

        # Passo 9: Clicar no checkbox da confirmação
        # Substitua X_CHECKBOX e Y_CHECKBOX pelas coordenadas corretas do seu computador
        X_CHECKBOX = 720
        Y_CHECKBOX = 514  
        pyautogui.click(X_CHECKBOX, Y_CHECKBOX)
        time.sleep(2)

        # Passo 9: Clicar em "Ignorar"
        # Substitua X_IGNORAR e Y_IGNORAR pelas coordenadas corretas do seu computador
        X_IGNORAR = 1034
        Y_IGNORAR = 549
        pyautogui.click(X_IGNORAR, Y_IGNORAR)
        time.sleep(2)

        print("Pasta '%Temp%' realizada com sucesso")

    except Exception as e:
        print(f"Ocorreu um erro durante a limpeza da pasta %Temp%: {e}")
        sys.exit(1)



def limpar_temp(deve_acontecer_temp):
    """
    Função para limpar a pasta Temp no Windows.
    """

    deve_acontecer = deve_acontecer_temp

    if not deve_acontecer:
        print("Pasta Temp desativada")
        return

    try:
        # Passo 2: Pressionar Win + R
        pyautogui.hotkey('win', 'r')
        time.sleep(2) 

        # Passo 3: Digitar 'recent'
        pyautogui.typewrite('temp', interval=0.05)
        time.sleep(2)

        # Passo 4: Pressionar Enter
        pyautogui.press('enter')
        time.sleep(3)  

        # Passo 5: Clicar nos arquivos
        # Substitua X_ARQUIVOS e Y_ARQUIVOS pelas coordenadas corretas do seu computador
        X_ARQUIVOS = 1547  
        Y_ARQUIVOS = 276 
        pyautogui.click(X_ARQUIVOS, Y_ARQUIVOS)
        time.sleep(2)

        # Passo 6: Selecionar todos os itens com Ctrl + A
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)

        # Passo 7: Pressionar Delete
        pyautogui.press('delete')
        time.sleep(10)

        # Passo 8: Clicar em continuar
        # Substitua X_ARQUIVOS e Y_ARQUIVOS pelas coordenadas corretas do seu computador
        X_ARQUIVOS = 895  
        Y_ARQUIVOS = 472
        pyautogui.click(X_ARQUIVOS, Y_ARQUIVOS)
        time.sleep(2)

        # Passo 9: Clicar no checkbox da confirmação
        # Substitua X_CHECKBOX e Y_CHECKBOX pelas coordenadas corretas do seu computador
        X_CHECKBOX = 725
        Y_CHECKBOX = 497  
        pyautogui.click(X_CHECKBOX, Y_CHECKBOX)
        time.sleep(2)

        # Passo 9: Clicar em "Ignorar"
        # Substitua X_IGNORAR e Y_IGNORAR pelas coordenadas corretas do seu computador
        X_IGNORAR = 1025
        Y_IGNORAR = 524 
        pyautogui.click(X_IGNORAR, Y_IGNORAR)
        time.sleep(2)

        print("Pasta Temp realizada com sucesso")

    except Exception as e:
        print(f"Ocorreu um erro durante a limpeza da pasta Temp: {e}")
        sys.exit(1)



def limpar_recent(deve_acontecer_recent):
    """
    Função para limpar a pasta Recent no Windows.
    """

    deve_acontecer = deve_acontecer_recent

    if not deve_acontecer:
        print("Pasta Recent desativada")
        return

    try:
        # Passo 2: Pressionar Win + R
        pyautogui.hotkey('win', 'r')
        time.sleep(2) 

        # Passo 3: Digitar 'recent'
        pyautogui.typewrite('recent', interval=0.05)
        time.sleep(2)

        # Passo 4: Pressionar Enter
        pyautogui.press('enter')
        time.sleep(3)  

        # Passo 5: Clicar nos arquivos
        # Substitua X_ARQUIVOS e Y_ARQUIVOS pelas coordenadas corretas do seu computador
        X_ARQUIVOS = 1547  
        Y_ARQUIVOS = 276 
        pyautogui.click(X_ARQUIVOS, Y_ARQUIVOS)
        time.sleep(2)

        # Passo 6: Selecionar todos os itens com Ctrl + A
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)

        # Passo 7: Pressionar Delete
        pyautogui.press('delete')
        time.sleep(10)

        # Passo 8: Clicar no checkbox da confirmação
        # Substitua X_CHECKBOX e Y_CHECKBOX pelas coordenadas corretas do seu computador
        X_CHECKBOX = 287 
        Y_CHECKBOX = 493  
        pyautogui.click(X_CHECKBOX, Y_CHECKBOX)
        time.sleep(2)

        # Passo 9: Clicar em "Ignorar"
        # Substitua X_IGNORAR e Y_IGNORAR pelas coordenadas corretas do seu computador
        X_IGNORAR = 600 
        Y_IGNORAR = 528  
        pyautogui.click(X_IGNORAR, Y_IGNORAR)
        time.sleep(2)

        print("Pasta Recent realizada com sucesso")

    except Exception as e:
        print(f"Ocorreu um erro durante a limpeza da pasta Recent: {e}")
        sys.exit(1)



def limpar_prefetch(deve_acontecer_prefetch):
    """
    Função para limpar a pasta Prefetch no Windows.
    """

    deve_acontecer = deve_acontecer_prefetch

    if not deve_acontecer:
        print("Prefetch desativada")
        return

    try:
        # Passo 2: Pressionar Win + R
        pyautogui.hotkey('win', 'r')
        time.sleep(2)

        # Passo 3: Digitar 'prefetch'
        pyautogui.typewrite('prefetch', interval=0.05)
        time.sleep(2)

        # Passo 4: Pressionar Enter
        pyautogui.press('enter')
        time.sleep(3)

        # Passo 5: Clicar em "Continuar" se solicitado
        # Substitua X_CONTINUAR e Y_CONTINUAR pelas coordenadas corretas do seu computador
        X_CONTINUAR = 968
        Y_CONTINUAR = 561  
        pyautogui.click(X_CONTINUAR, Y_CONTINUAR)
        time.sleep(2)

        # Passo 6: Clicar nos arquivos (selecionar a janela da pasta)
        # Substitua X_ARQUIVOS e Y_ARQUIVOS pelas coordenadas corretas do seu computador
        X_ARQUIVOS = 1547  
        Y_ARQUIVOS = 276 
        pyautogui.click(X_ARQUIVOS, Y_ARQUIVOS)
        time.sleep(2)

        # Passo 7: Selecionar todos os itens com Ctrl + A
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(2)

        # Passo 8: Pressionar Delete
        pyautogui.press('delete')
        time.sleep(10)

        # Passo 9: Clicar no checkbox da confirmação
        # Substitua X_CHECKBOX e Y_CHECKBOX pelas coordenadas corretas do seu computador
        X_CHECKBOX = 287 
        Y_CHECKBOX = 493  
        pyautogui.click(X_CHECKBOX, Y_CHECKBOX)
        time.sleep(2)

        # Passo 10: Clicar em "Ignorar"
        # Substitua X_IGNORAR e Y_IGNORAR pelas coordenadas corretas do seu computador
        X_IGNORAR = 600 
        Y_IGNORAR = 528  
        pyautogui.click(X_IGNORAR, Y_IGNORAR)
        time.sleep(2)

        print("Pasta Prefetch realizada com sucesso")

    except Exception as e:
        print(f"Ocorreu um erro durante a limpeza da pasta Prefetch: {e}")
        sys.exit(1)
