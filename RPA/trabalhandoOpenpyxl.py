from openpyxl import load_workbook
import os

arquivo = 'E:\\Faculdade\\Curso Python\\excell\\DeletarLinhaColuna.xlsx'
planilha = load_workbook(arquivo)

sheet_selecionada = planilha['Aluno']
sheet_selecionada.delete_rows(5)
sheet_selecionada.delete_cols(2)

planilha.save(arquivo)

os.startfile(arquivo)