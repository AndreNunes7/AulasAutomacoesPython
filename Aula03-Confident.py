import pyautogui 

print(pyautogui.locateOnScreen("env/Aulas/button_5.png", confidence=0.8)) # arruma diferenças insignificantes dos pixels ( confidence)

print(pyautogui.locateOnScreen("env/Aulas/button_5.png", grayscale=True)) # desatura as cores da tela e ganha performance porem potencializa a chance de falsos positivos (grayscale)