from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

webdriver = webdriver.Chrome()
webdriver.get('https://pt.surveymonkey.com/r/WLXYDX2')

pyautogui.sleep(3)

nome = webdriver.find_element(By.NAME, "166517069")
pyautogui.sleep(1)
nome.send_keys("João")
pyautogui.sleep(1)
email = webdriver.find_element(By.NAME, "166517072")
pyautogui.sleep(1)
email.send_keys("joao@email.com")
pyautogui.sleep(1)
telefone = webdriver.find_element(By.NAME, "166517070")
pyautogui.sleep(1)
telefone.send_keys("11999999999")
pyautogui.sleep(1)
sobre = webdriver.find_element(By.NAME, "166517073")
pyautogui.sleep(1)
radio_button = webdriver.find_element(By.ID, "166517071_1215509812_label")
pyautogui.sleep(1)
radio_button.click()
pyautogui.sleep(1)
sobre.send_keys("lore ipsum")
pyautogui.sleep(3)
enviar = webdriver.find_element(By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')
enviar.click()
pyautogui.sleep(3)
