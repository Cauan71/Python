import openpyxl
from docxtpl import DocxTemplate
import datetime





# Acessar a planilha e consumir os dados
# Arquivo que deseja acessar
caminho = 'Planilha_Py.xlsx'

# Carregar a planilha e abrir
pasta_trabalho = openpyxl.load_workbook(caminho)

# Selecionar a planilha ativa   
planilha = pasta_trabalho.active

valores = list(planilha.values)
print(valores)

# Abrir o documento docx (cerficado)
caminho_docx = 'certificate.docx'
doc = DocxTemplate(caminho_docx)

# [1:] Ignora o cabeçalho da planilha (Nome, Curso, Data, Instrutor)
for x in valores[1:]:
    
    # Imprime no arquivo o nome, curso, data e instrutor
    doc.render({
        'nome': x[0], # Posição da planilha
        'curso': x[1],
        'data': x[2].strftime('%d/%m/%Y'),
        'instrutor': x[3]
        
    })
    
    nome = f'cerficado de {x[0]}.docx'
    doc.save(nome)
