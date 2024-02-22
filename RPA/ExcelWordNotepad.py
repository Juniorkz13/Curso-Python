import subprocess
import pyautogui

def open_application(application_path):
    subprocess.Popen(application_path)

# Caminho para o aplicativo que você deseja abrir
excel_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE'
word_path = 'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE'
notepad_path = 'C:\\Windows\\System32\\notepad.exe'

# Dicionário para mapear a escolha do usuário para o caminho do aplicativo
app_paths = {"Excel": excel_path, "Word": word_path, "Notepad": notepad_path}

# Solicitar ao usuário que escolha um aplicativo para abrir
app_choice = pyautogui.confirm(text='Qual aplicativo você deseja abrir?', title='Escolha do aplicativo', buttons=['Excel', 'Word', 'Notepad'])

# Abrir o aplicativo escolhido
open_application(app_paths[app_choice])
