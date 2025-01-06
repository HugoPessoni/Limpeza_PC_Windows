import pyautogui
import time

# Obter a posição atual do cursor
# Imprimir a posição
while True:
    posicao_atual = pyautogui.position()
    print("Posição atual do cursor (x/y):", posicao_atual)
    time.sleep(2)