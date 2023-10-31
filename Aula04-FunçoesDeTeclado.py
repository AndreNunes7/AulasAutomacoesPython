import pyautogui

# typewrite() = Aceita um parametro de string e digita-os em caracteres

print(pyautogui.position())
pyautogui.click(x=213, y=490, duration=2) 
pyautogui.typewrite("Hello world", interval=0.5)  # ( interval ) - coloca um intervalo na digitação da frase
pyautogui.press("enter")
pyautogui.typewrite("Linha2", interval=0.5)
print(pyautogui.KEYBOARD_KEYS) # mostra o nome de todas as teclas do teclado



# Atalhos 1 forma:

# pressionando os botoes e segurando-os

pyautogui.keyDown("ctrl")
pyautogui.keyDown("alt")
pyautogui.keyDown("tab")


# Soltando os botoes na ordem inversa 

pyautogui.keyUp("tab")
pyautogui.keyUp("alt")
pyautogui.keyUp("ctrl")


# atalhos 2 forma:


pyautogui.hotkey("ctrl", "alt", "tab")