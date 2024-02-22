import xlsxwriter
import os

arquivo = 'E:\\Faculdade\\Curso Python\\Formulas.xlsx'
workbook = xlsxwriter.Workbook(arquivo)
sheetPadrao = workbook.add_worksheet()

sheetPadrao.write("A1", "Número 1")
sheetPadrao.write("B1", "Número 2")
sheetPadrao.write("C1", "Fórmula")

sheetPadrao.write("A2", 10)
sheetPadrao.write("A3", 6)
sheetPadrao.write("A4", 8)
sheetPadrao.write("A5", 5)
sheetPadrao.write("A6", 'José')

sheetPadrao.write("B2", 7)
sheetPadrao.write("B3", 5)
sheetPadrao.write("B4", 3)
sheetPadrao.write("B5", 1)
sheetPadrao.write("B6", 'Júnior')

sheetPadrao.write("C2", '=A2+B2')
sheetPadrao.write("C3", '=A3-B3')
sheetPadrao.write("C4", '=A4*B4')
sheetPadrao.write("C5", '=A5/B5')
sheetPadrao.write("C6", '=CONCATENATE(A6, " ", B6)')

#tamanho da coluna
sheetPadrao.set_column('A:C', 20)

workbook.close()

os.startfile(arquivo)
