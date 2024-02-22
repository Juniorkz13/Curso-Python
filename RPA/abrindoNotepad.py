import pyautogui as pa

pa.hotkey('winleft', 'r')
pa.write('notepad')
pa.press('enter')
pa.sleep(2)
pa.typewrite('Ola mundo!')
pa.sleep(5)
fecharJanela = pa.getActiveWindow()
fecharJanela.close()