#Primeiro commit

print('--------------------------------------')
print('  Bem-vindo(a) a FICHA DE ANAMNESE!   ')
print('--------------------------------------')
print('')
print('')
print('*******  DADOS PESSOAIS DO CLIENTE  *******')
print('')
nome_cliente = str(input('Digite o primeiro nome do cliente: '))
sobrenome_cliente = str(input('Digite o último nome do cliente: '))
data_nascimento_dia = int(input('Digite o dia que o cliente nasceu: '))
data_nascimento_mes = int(input('Digite o mês que o cliente nasceu: '))
data_nascimento_ano = int(input('Digite o ano que o cliente nasceu: '))
contato_cliente = str(input('Digite o número para contato: '))
email_cliente = str(input('Digite o email do clinte: '))

print('')
print('*******  AVALIAÇÃO  *******')
print('')
print('Tipo de calçado mais utilizado:')
print('[1] Aberto')
print('[2] Fechado')
calcado = int(input('Digite a opção: '))

print('')
print('Usa meia com frequência?')
print('[1] Sim')
print('[2] Não')
meia_freq = int(input('Digite a opção: '))

if meia_freq == 1:
    print('')
    print('Tipo de meia:')
    print('[1] Social')
    print('[2] Comum')
    meia_tipo = int(input('Digite a opção: '))

print('')
print('Cirurgia nos membros inferiores?')
print('[1] Sim')
print('[2] Não')
cirurgia = int(input('Digite a opção: '))

if cirurgia == 1:
    print('')
    cirurgia_tipo = str(input('Especifique: '))

print('')
print('Está tomando algum medicamento?')
print('[1] Sim')
print('[2] Não')
medicamento = int(input('Digite a opção: '))

if medicamento == 1:
    print('')
    medicamento_tipo = str(input('Especifique: '))

print('')
print('Possui alguma alergia?')
print('[1] Sim')
print('[2] Não')
alergia = int(input('Digite a opção: '))

if alergia ==1:
    print('')
    alergia_tipo = str(input('Especifique: '))

print('')
print('Está gestante?')
print('[1] Sim')
print('[2] Não')
gestante = int(input('Digite a opção: '))

if gestante == 1:
    print('')
    gestante_tempo = str(input('Digite o número de semana ou meses (especifique)'))

print('')
print('Tem HIPOTENSÃO?')
print('[1] Sim')
print('[2] Não')
hipotensao = int(input('Digite a opção: '))

print('')
print('Tem HIPERTENSÃO?')
print('[1] Sim')
print('[2] Não')
hipertensao = int(input('Digite a opção: '))

print('')
print('Tem HANSENIASE?')
print('[1] Sim')
print('[2] Não')
hanseniase = int(input('Digite a opção: '))

print('')
print('Tem algum tipo de câncer?')
print('[1] Sim')
print('[2] Não')
cancer = int(input('Digite a opção: '))

print('')
print(' Tem Distúrbio circulatório?')
print('[1] Sim')
print('[2] Não')
disturbio_circulatorio = int(input('Digite a opção: '))

print('')
print('tem DIABETES?')
print('[1] Sim')
print('[2] Não')
diabetes = int(input('Digite a opção: '))

print('')
print('Você é cardiopata?')
print('[1] Sim')
print('[2] Não')
cardiopata = int(input('Digite a opção: '))

print('')
print('Você é portador de marca-passo?')
print('[1] Sim')
print('[2] Não')
marca_passo = int(input('Digite a opção: '))

print('')
print('Você é portador de pinos?')
print('[1] Sim')
print('[2] Não')
pinos = int(input('Digite a opção: '))

print('')
print('Tem HEPATITE?')
print('[1] Sim')
print('[2] Não')
hepatite = int(input('Digite a opção: '))

print('')
print('Possue sensibilidade (fora do normal) nos pés?')
print('[1] Sim')
print('[2] Não')
sensibilidade_pes = int(input('Digite a opção: '))

print('')
print('****************************************************************************************************')
print('EXISTE ALGUM PROBLEMA QUE JULGA SER NECESSÁRIO INFORMAR AO PROFFISSIONAL ANTES DO PROCEDIMENTO?')
print('[1] Sim')
print('[2] Não')
mais_informacoes = int(input('Digite a opção: '))

if mais_informacoes == 1:
    mais_informacoes_detalhes = str(input('Escreva mais detalhes sobre: '))



















