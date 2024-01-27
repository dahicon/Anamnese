#Primeiro commit

print('--------------------------------------')
print('  Bem-vindo(a) a FICHA DE ANAMNESE!   ')
print('--------------------------------------')
print('')
print('')
print('DADOS PESSOAIS DO CLIENTE')
print('')
nome_cliente = str(input('Digite o primeiro nome do cliente: '))
sobrenome_cliente = str(input('Digite o último nome do cliente: '))
data_nascimento_dia = int(input('Digite o dia que o cliente nasceu: '))
data_nascimento_mes = int(input('Digite o mês que o cliente nasceu: '))
data_nascimento_ano = int(input('Digite o ano que o cliente nasceu: '))
contato_cliente = str(input('Digite o número para contato: '))
email_cliente = str(input('Digite o email do clinte: '))

print('')
print('AVALIAÇÃO')
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