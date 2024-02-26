from openpyxl import load_workbook
import os

arquivo = 'E:\\Faculdade\\Curso Python\\excell\\Formulas2.xlsx'
planilha = load_workbook(arquivo)

sheet_selecionada = planilha['Aluno']

sheet_selecionada['A6'] = '=SUM(A2:A5)'
sheet_selecionada['B6'] = '=SUM(B2:B5)'
sheet_selecionada['D2'] = '=A2+B2'
sheet_selecionada['D3'] = '=A3-B3'
sheet_selecionada['D4'] = '=A4*B4'
sheet_selecionada['D5'] = '=A5/B5'

sheet_selecionada['B12'] = '=MID(A12,1,3)'
sheet_selecionada['C12'] = '=MID(A12,5,3)'
sheet_selecionada['D12'] = '=MID(A12,9,3)'
sheet_selecionada['E12'] = '=MID(A12,13,2)'


planilha.save(arquivo)

os.startfile(arquivo)