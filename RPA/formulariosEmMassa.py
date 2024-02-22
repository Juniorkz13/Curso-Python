from selenium import webdriver as wd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from openpyxl import load_workbook

nomeCaminhoArquivo = 'E:\Faculdade\Curso Python\DadosFormulario.xlsx'
planilha_aberta = load_workbook(nomeCaminhoArquivo)
sheet_selecionada = planilha_aberta['Dados']

for linha in range(2, len(sheet_selecionada['A']) + 1):
    nome = sheet_selecionada[f'A{linha}'].value
    email = sheet_selecionada[f'B{linha}'].value
    telefone = sheet_selecionada[f'C{linha}'].value
    sexo = sheet_selecionada[f'D{linha}'].value
    sobre = sheet_selecionada[f'E{linha}'].value

    webdriver = wd.Chrome()
    webdriver.get('https://pt.surveymonkey.com/r/WLXYDX2')

    espera = WebDriverWait(webdriver, 10)
    campo_nome = espera.until(ec.presence_of_element_located((By.NAME, "166517069")))
    campo_nome.send_keys(nome)
    campo_email = webdriver.find_element(By.NAME, "166517072")
    campo_email.send_keys(email)
    campo_telefone = webdriver.find_element(By.NAME, "166517070")
    campo_telefone.send_keys(telefone)
    campo_sobre = webdriver.find_element(By.NAME, "166517073")
    campo_sobre.send_keys(sobre)
    if sexo == 'Feminino':
        botao_feminino = espera.until(ec.element_to_be_clickable((By.ID, "166517071_1215509813_label")))
        botao_feminino.click()
    else:
        botao_masculino = espera.until(ec.element_to_be_clickable((By.ID, "166517071_1215509812_label")))
        botao_masculino.click()
    botao_enviar = espera.until(ec.element_to_be_clickable((By.XPATH, '//*[@id="patas"]/main/article/section/form/div[2]/button')))