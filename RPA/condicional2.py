import xlsxwriter
import os

arquivo = 'E:\\Faculdade\\Curso Python\\FormatacaoCondicionalIcones.xlsx'
workbook = xlsxwriter.Workbook(arquivo)
sheetPadrao = workbook.add_worksheet()

inserirDados = [
    [ 'Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4' ],
    [ 1, 10, 3, 14 ],
    [ 5, 6, 2, 8 ],
    [ 9, 10, 11, 12 ],
    [ 13, 4, 15, 16 ],
    [ 97, 54, 55, 13 ]
]

sheetPadrao.write('A1','Formatação com Icones')

for linha, range in enumerate(inserirDados):
    sheetPadrao.write_row(linha + 2, 1, range)

sheetPadrao.conditional_format('B4:E4', {'type': 'icon_set', 'icon_style': '3_traffic_lights'})
sheetPadrao.conditional_format('B5:E5', {'type': 'icon_set', 'icon_style': '3_traffic_lights', 'reverse_icons': True})
sheetPadrao.conditional_format('B6:E6', {'type': 'icon_set', 'icon_style': '3_arrows'})
sheetPadrao.conditional_format('B7:E7', {'type': 'icon_set', 'icon_style': '4_arrows'})
sheetPadrao.conditional_format('B8:E8', {'type': 'icon_set', 'icon_style': '5_ratings'})

workbook.close()

os.startfile(arquivo)
