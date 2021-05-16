'''Autora: Helena Maruf'''
'''Data: 03/04/2021'''
'''Nome do arquivo: oraculo_sincero.py'''
'''Descrição: este código é uma implementação em modo script de um Oráculo (bem) sincero.'''
'''Funcionamento:
    --> O usuário digita uma pergunta.
    --> O oráculo irá responder com um "NÃO!", "SIM!" ou "TALVEZ...".
    --> O usuário pode fazer quantas perguntas quiser e o oráculo irá respondê-las uma por uma.
    --> Se o usuário apertar a tecla zero, o oráculo mostrará uma dica e a execução do código será encerrada.
    --> Exemplo de rodada:
            1. Usuário digita "Oráculo, você acha que eu devo tomar banho?".
            2. Oráculo responde: "NÃO!".
            3. No campo da próxima pergunta, o usuário tecla "0" para sair.
            4. Oráculo mostra a dica: "Se toca e não me enche!".
            5. Execução finalizada.
    --> AVISO: se você tomar qualquer decisão com base
        no oráculo, a responsabilidade será TODA SUA! >:) '''
    

from random import choice

def titulo(caractere = '*', total = 60):
    linha = caractere * total
    print(linha)
    print(f'             ORÁCULO SINCERO - A VERDADE DÓI!')
    print(linha)
    print()

def pergunta_ou_sai():
    escolha = input('PERGUNTA [Tecle 0 para sair]: ')
    return escolha

def resposta():
    lista = ['NÃO!', 'SIM!', 'TALVEZ...']
    print(f'RESPOSTA - {choice(lista)}')
    print()

def dica_do_oraculo():
    lista = ['Relaxa... Nada vai dar certo!',
             'Melhor ser rico com saúde do que pobre doente.',
             'Deu ruim? Reze para fuDeus!',
             'Não deixe para hoje aquilo que você pode fazer amanhã!',
             'Dinheiro não traz felicidade... Dê-me o seu e seja feliz!',
             'Uma coisa é uma coisa, outra coisa é outra coisa.',
             'Vai estudar!',
             'Se toca e não me enche!',
             'Lavou, tá novo!',
             'O que é um peido pra quem tá cagado?',
             'Aquilo é uma estrela ou um drone?',
             'Se você está ferrado(a), lembre-se: sempre existe alguém mais ferrado que você!',
             'A Seita do pobre = "A Seita" vale refeição?',
             'Tome água, pois lágrimas vão rolar...']
    print()
    print(f'******Dica do Oráculo: {choice(lista)}')
    
def main():
    titulo()
    while True:
        Escolha = pergunta_ou_sai()
        if Escolha == '0':
            break
        resposta()
    dica_do_oraculo()

if __name__ == '__main__':
    main()
