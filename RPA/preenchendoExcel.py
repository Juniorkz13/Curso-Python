import xlsxwriter
import os

arquivo = 'E:\\Faculdade\\Curso Python\\PrimeiroExemplo.xlsx'
workbook = xlsxwriter.Workbook(arquivo)
sheetPadrao = workbook.add_worksheet()

# corFundo = workbook.add_format({'fg_color': 'yellow'})
# corFonte = workbook.add_format({'font_color': 'red'})

formatacao = workbook.add_format({'bold': True, 'font_color': 'red', 'bg_color': 'yellow', 'border': 1})
formatacao2 = workbook.add_format({'font_color': 'blue', 'border': 1})

sheetPadrao.write("A1", "Nome", formatacao)
sheetPadrao.write("B1", "Idade", formatacao)
sheetPadrao.write("A2", "Amanda", formatacao2)
sheetPadrao.write("B2", 21, formatacao2)
sheetPadrao.write("A3", "Allan", formatacao2)
sheetPadrao.write("B3", 28, formatacao2)

workbook.close()

os.startfile(arquivo)
