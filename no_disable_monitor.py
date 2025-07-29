import pyautogui

# Este script pressiona a tecla 'f13' a cada 5 segundos para evitar que o monitor seja desligado automaticamente.
# Útil para manter o computador ativo durante longos períodos de inatividade.

while True:
    pyautogui.press('f13')  # Simula o pressionamento da tecla F13
    pyautogui.sleep(5)      # Aguarda 5 segundos antes de repetir

