import xlsxwriter
import os

arquivo = 'E:\\Faculdade\\Curso Python\\MergeCells.xlsx'
workbook = xlsxwriter.Workbook(arquivo)
sheetPadrao = workbook.add_worksheet()

add_merge_cells = workbook.add_format({
    'bold': True,
    'border': 1,
    'align': 'center',
    'valign': 'vcenter',
    'fg_color': 'yellow',
    'size': 30,
    'font_color': 'red'
})

sheetPadrao.merge_range('A1:I1', 'José Júnior', add_merge_cells)

workbook.close()

os.startfile(arquivo)
