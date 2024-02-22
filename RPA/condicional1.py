import xlsxwriter
import os

arquivo = 'E:\\Faculdade\\Curso Python\\FormatacaoCondicional.xlsx'
workbook = xlsxwriter.Workbook(arquivo)
sheetPadrao = workbook.add_worksheet()

formatacaoMaior = workbook.add_format({'bold': True, 'bg_color': 'green'})
formatacaoMenor = workbook.add_format({'bold': True, 'bg_color': 'red'})

inserirDados = [
    [ 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4' ],
    [ 1, 10, 3, 14 ],
    [ 5, 6, 2, 8 ],
    [ 9, 10, 11, 12 ],
    [ 13, 4, 15, 16 ]
]

sheetPadrao.write('A1','Células menores que 5 e maiores que 5')

for linha, range in enumerate(inserirDados):
    sheetPadrao.write_row(linha + 2, 1, range)

sheetPadrao.conditional_format('B4:E7', {'type': 'cell', 'criteria': '>=', 'value': 5, 'format': formatacaoMaior})
sheetPadrao.conditional_format('B4:E7', {'type': 'cell', 'criteria': '<', 'value': 5, 'format': formatacaoMenor})

workbook.close()

os.startfile(arquivo)
