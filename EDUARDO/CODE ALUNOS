import random
from datetime import date 

alunos = ['Eduardo','Vinicius','Marjori','Gabriel','Arthur','Mateus','Alan','Lucas','Fernando','Mariane','Leonardo','Luiz','Mileni']
alunos.sort()
presenca = ['']
Presentes = []
date_atual = date.today()

file = open('lista de presenca.csv', 'w')


print('Ola Professor Lucas! Vamos começar com a chamada de hoje'.center(100,'='))
print('\n')
print('LISTA ALUNOS SINTEC'.center(60,'='))
print('-'*60)

for i in range(len(alunos)):
    print(alunos[i].center(60,' '))
    print('-'*60)

print('='*60)
print('\n')

pos = 0
for a in range(len(alunos)):
    chamada = str(input(f'O aluno {alunos[pos]} está presente? [S/N]:')).upper()
    print('='*50)

    if chamada == 'S':
        Presentes.append(alunos[pos])
        presenca.append('+')
        
    else:
        presenca.append('-')
    pos += 1

for i in range(len(alunos)):
    file.write(alunos[i] + presenca[i] + '\n')

Presentes_2 = list(Presentes)


print('='*60)
print('\n')
print('='*60)
print('OK CHAMADA FEITA VAMOS PARA AS QUESTOES'.center(60,'='))
print('='*60)
quest = int(input('Quantas questoes seram feitas hoje professor?:'))
print('='*60)

for q in range(0,quest):
    choice_2 = random.choice(Presentes_2)
    print(f'O aluno escolhido para responder a quetão {q+1} foi {choice_2}')
    print('='*60)
    
    if q == quest-1:
        break  

    next =(str(input('Podemos prosseguir para proxima questão professor? [S/N]'))).upper()
    print('-'*60)
    Presentes_2.remove(choice_2)
    
    if next == 'N':
        print('OK as questões foram respondidas')
        break
    if len(Presentes_2) == 1 :
        Presentes_2 = list(Presentes)

print('\n')
print('='*60)
print('OK as questões foram respondidas'.center(60,'='))
print('='*60)
