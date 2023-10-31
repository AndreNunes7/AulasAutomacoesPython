import pyautogui

teste = pyautogui.size()  # verifica o tamanho da tela
posicao = pyautogui.position()   # ve a posição que o mouse esta
posicao_9 = pyautogui.position()


pyautogui.moveTo(x= -1920, y=1079, duration=2); pyautogui.click()  # ira mover o mouse para as coordenadas indicadas e no fical irar clicar
pyautogui.moveTo(x= -1920, y=1079); pyautogui.rightClick()

pyautogui.dragTo(150,150, duration=3) # Método utilizado para mover e arrastar o ponteiro do mouse para uma coordenada específica


pyautogui.dragRel(150, 150) # Clica e arrasta o mouse para uma posição relativa a posição do mouse atual


pyautogui.moveRel(159, 200) # Move o cursor do mouse para uma posição relativa a posição do mouse atual



pyautogui.displayMousePosition() # ira ficar analisando a posição do mouse a todo instante, Use esta opçao!

print(posicao_9)
