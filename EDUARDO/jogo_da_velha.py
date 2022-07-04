import random

board=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

print('-'*85)
print('x-o'*10,'JOGO DA VELHA PLAYER X MAQUINA EM PYTHON','x-o'*10)
print('-'*85,'\n')

print('='*10,'TABULEIRO','='*10)

def tabuleiro():
    print('-'*7)
    for i in board:
        for j in i:
            print(f'|{j}',end='')
        print('|')
    print('-'*7,'\n')


def winer1():
    #PRIMEIRA LINHA
        if board[0][0] + board[0][1] + board[0][2] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()
    #SEGUNDA LINHA
        elif board[1][0] + board[1][1] + board[1][2] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()
    #TERCEIRA LINHA
        elif board[2][0] + board[2][1] + board[2][2] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()
    #PRIMEIRA COLUMA
        elif board[0][0] + board[1][0] + board[2][0] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()
    #SEGUNDA COLUNA
        elif board[0][1] + board[1][1] + board[2][1] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()
    #TERCEIRA COLUNA
        elif board[0][2] + board[1][2] + board[2][2] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()
    #DIAGONAL E/D
        elif board[0][0] + board[1][1] + board[2][2] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()
    #DIAGONAL D/E
        elif board[0][2] + board[1][1] + board[2][0] == 'xxx':
            print('`'*10,'Jogador 1 venceu!','`'*10)
            exit()


def winer2():
#PRIMEIRA LINHA
    if board[0][0] + board[0][1] + board[0][2] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()
#SEGUNDA LINHA
    elif board[1][0] + board[1][1] + board[1][2] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()
#TERCEIRA LINHA
    elif board[2][0] + board[2][1] + board[2][2] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()
#PRIMEIRA COLUMA
    elif board[0][0] + board[1][0] + board[2][0] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()
#SEGUNDA COLUNA
    elif board[0][1] + board[1][1] + board[2][1] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()
#TERCEIRA COLUNA
    elif board[0][2] + board[1][2] + board[2][2] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()
#DIAGONAL E/D
    elif board[0][0] + board[1][1] + board[2][2] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()
#DIAGONAL D/E
    elif board[0][2] + board[1][1] + board[2][0] == 'ooo':
        print('`'*10,'Jogador 2 venceu!','`'*10)
        exit()    


while True:
    player = 'x'
    if player == 'x':
        print('VEZ DO JOGADOR 1')
        while True:
            try:                # Erro de valor e de letras
                print('-'*20)
                line = int(input('Digite a linha que deseja:'))
                columns = int(input('DIgite a coluna que deseja:'))
                print('-'*20)
                if line or columns :
                    ValueError
            except ValueError:
                print('Desculpe nosso jogo aceita apenas  NUMEROS de 1 a 3!!!')
            
            else:
                if line > 1 or line < 3 or columns < 1 or columns > 3 :
                  while line < 1 or line >3 or columns < 1 or columns > 3 :
                        print('Desculpe nosso jogo aceita apenas  NUMEROS de 1 a 3!!!')
                        line = int(input('Digite a linha que deseja:'))
                        columns = int(input('DIgite a coluna que deseja:'))

                if board[line-1] [columns-1] == ' ':        # Verificação de espaço
                        board[line-1] [columns-1] = player
                else:
                    print('Local ja ocupado! Tente jogar em outro!')
                    continue # A função continue faz com que o while criado no começo da jogada de cada jogador
            tabuleiro()
            winer1()
            break
        player = 'o'
    if player == 'o':        #Player 2
        print('VEZ DA MAQUINA')
        while True:
            print('-'*20)
            line = random.randint(1,3)
            print(f'Maquina escolheu a linha {line}')
            columns = random.randint(1,3)
            print(f'Maquina escolheu a coluna {columns}')
            print('-'*20)
            if board[line-1] [columns-1] == ' ':  
                board[line-1] [columns-1] = player
            else:
                continue
            tabuleiro()
            winer2()
            break
        player='x'