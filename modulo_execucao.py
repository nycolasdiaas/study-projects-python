# Importação da Biblioteca de Mensagens
import modulo_mensagens

# Dicionário e Listas (Informações dos Pacientes)
dados = dict()
doencas = list()

# Coleta de Dados e Inserção em Dicionário e Lista
def dadosPessoais():
    while True:
        nome = str(input('Informe o seu nome: ')).strip().upper()
        if nome.isalpha() is True:
            dados['nome'] = nome
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados["idade"] = int(input(f'{dados["nome"]}, informe a sua idade (em anos): '))
        if dados["idade"] >= 1 and dados["idade"] < 120:
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['fumante'] = str(input(f'{dados["nome"]}, você é fumante [s/n]: ')).strip().upper()[0]
        if dados['fumante'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    
def dadosDoencas():
    while True:
        dados['hipertensao'] = str(input(f'A) Você é hipertenso? [S/N]: ')).strip().upper()[0]
        if dados['hipertensao'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['asma'] = str(input(f'B) Você é asmatico? [S/N]: ')).strip().upper()[0]
        if dados['asma'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['diabetes'] = str(input(f'C) Você é diabético(a) [s/n]: ')).strip().upper()[0]
        if dados['diabetes'] in 'SN':
            break
        else:
            modulo_mensagens.errodado() 
        
def dadosSintomas():
    while True:
        dados['tosse'] = str(input(f'A) Você está com tosse seca? [s/n]: ')).strip().upper()[0]  
        if dados['tosse'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['cansaço'] = str(input(f'B) Você está com cansaço excessivo? [s/n]: ')).strip().upper()[0]
        if dados['cansaço'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['febre'] = str(input(f'C) Você está com febre persistente? [s/n]: ')).strip().upper()[0]
        if dados['febre'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['respiração'] = str(input(f'D) Você está com dificuldade de respirar? [s/n]: ')).strip().upper()[0]
        if dados['respiração'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
 
# Análise de Dados para Relatório           

def analiseCaso1():
    if dados['idade'] >= 60:
        modulo_mensagens.grim60()
        if dados['fumante'] == 'S':
            modulo_mensagens.msgfumantes()
        else:
            modulo_mensagens.msgfumanten()
    else:
        modulo_mensagens.gri()
        if dados['fumante'] == 'S':
            modulo_mensagens.msgfumantes()
        else:
            modulo_mensagens.msgfumanten()

def analiseCaso2():
    if dados['hipertensao'] == 'S':
        doencas.append(str('HIPERTENSÃO'))
    if dados['asma'] == 'S':
        doencas.append(str('ASMA'))
    if dados['diabetes'] == "S":
        doencas.append(str('DIABETES'))
    if doencas == []:
        modulo_mensagens.msgdoencasn()
    else:
        modulo_mensagens.msgdoencass()
        
def analiseCompleta():
    sintomasgraves = 0
    if dados['febre'] == 'S':
        sintomasgraves += 1
    if dados['respiração'] == 'S':
        sintomasgraves += 1
    if sintomasgraves == 1 or sintomasgraves == 2:
        modulo_mensagens.msgsintomasgraves()
    
    if dados['febre'] == 'N' and dados['respiração'] == 'N':
        sintomasleves = 0
        if dados['tosse'] == 'S':
            sintomasleves += 1
        if dados['cansaço'] == 'S':
            sintomasleves += 1
        if sintomasleves == 0:
            modulo_mensagens.msgsemsintomas()
        if sintomasleves == 1 or sintomasleves == 2:
            modulo_mensagens.msgsintomasleves()
            
def log_erro(msg):
    with open('./Sintoma-Covid/log_erro.txt', 'a+') as file:
        file.write(f'{msg}\n')