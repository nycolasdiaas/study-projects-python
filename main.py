# Importação do Módulo
import modulo_execucao
import modulo_mensagens

# main
try:
    modulo_mensagens.titulos('SISTEMA DE AJUDA NO DIAGNÓSTICO DA COVID-19')
    modulo_execucao.dadosPessoais()
    modulo_mensagens.titulos(f'DOENÇAS PRÉ-EXISTENTES')
    modulo_execucao.dadosDoencas()
    modulo_mensagens.titulos('SINTOMAS APRESENTADOS')
    modulo_execucao.dadosSintomas()
    
except Exception as erro:
    modulo_mensagens.errogenerico()
    modulo_execucao.log_erro(erro)

else:
    modulo_mensagens.titulos('RELATÓRIO DOS DADOS INFORMADOS')
    modulo_mensagens.cabeçalhorel()
    modulo_execucao.analiseCaso1()
    modulo_execucao.analiseCaso2()
    modulo_execucao.analiseCompleta()
    
finally:
    modulo_mensagens.titulos('FIQUE EM CASA, NÓS VAMOS SUPERAR!')
    modulo_mensagens.títulos('LAVE AS MÃOS, USE MÁSCARA E EVITE SAIR DE CASA!')
    modulo_mensagens.títulos('OBRIGADO POR UTILIZAR O SISTEMA!')