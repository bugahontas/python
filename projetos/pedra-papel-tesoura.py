from random import randint
import verificadores as vrf

opcoes = {0: 'PEDRA',
          1: 'PAPEL',
          2: 'TESOURA'}

def menu(caractere = '=', qtd = 29):
    print(caractere * qtd)
    print('   PEDRA----------Tecle [0]   ')
    print('   PAPEL----------Tecle [1]   ')
    print('  TESOURA---------Tecle [2]   ')
    print(caractere * qtd)

def usuario_escolhe(): 
    usuario = int(input('Qual você escolhe? '))
    return usuario

def pc_escolhe():
    pc = randint(0, 2)
    return pc

def placar(usuario, pc, caractere = '-', qtd = 25):
    print()
    print()
    print(caractere * qtd)
    print('         PLACAR        ')
    print(caractere * qtd)
    print(f'   {opcoes[usuario]}  X  {opcoes[pc]}')
    print(caractere * qtd)

def mensagem_final(usuario, pc):
    print()
    if opcoes[usuario] == opcoes[pc]:
        print(f'  RESULTADO = {vrf.empate()}')
    else:
        print('   VENCEDOR = ', end = '')
        if opcoes[usuario] == 'PEDRA':
            print(vrf.pedra(pc))
        elif opcoes[usuario] == 'PAPEL':
            print(vrf.papel(pc))
        else:
            print(vrf.tesoura(pc))

def main():
    menu()
    Usuario = usuario_escolhe()
    Pc = pc_escolhe()
    placar(Usuario, Pc)
    mensagem_final(Usuario, Pc)
    
if __name__ == '__main__':
    main()
