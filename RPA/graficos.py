import xlsxwriter
import os

arquivo = 'E:\\Faculdade\\Curso Python\\graficos.xlsx'
workbook = xlsxwriter.Workbook(arquivo)
sheetPadrao = workbook.add_worksheet()

bold = workbook.add_format({'bold': 1})

titulos = ['Categoria', 'Valores']
dados = [
    ['A', 'B', 'C', 'D', 'E'],
    [1, 2, 3, 4, 5]
]

sheetPadrao.write_row('A1', titulos, bold)
sheetPadrao.write_column('A2', dados[0])
sheetPadrao.write_column('B2', dados[1])

chart = workbook.add_chart({'type': 'column'})

chart.add_series({
    'name': 'Gráfico de Barras',
    'categories': '=Sheet1!$A$2:$A$6',
    'values': '=Sheet1!$B$2:$B$6'
})

sheetPadrao.insert_chart('C2', chart)

###############################

chart2 = workbook.add_chart({'type': 'area', 'subtype': 'stacked'})

chart2.add_series({
    'name': 'Gráfico de Área',
    'categories': '=Sheet1!$A$2:$A$6',
    'values': '=Sheet1!$B$2:$B$6'
})

sheetPadrao.insert_chart('C20', chart2)






workbook.close()

os.startfile(arquivo)
