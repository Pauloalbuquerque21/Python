from time import sleep
inf = list()
print('-='*20)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(0,11):
    print(f'{c}',end=' ', flush = True)
    sleep(0.5)
print('FIM')
print('-='*20)
print('Agora é sua vez de personalizar a contagem')
inf.append(int(input('Início:')))
inf.append(int(input('Fim:')))
inf.append(int(input('Passo:')))
if inf[0]>inf[1] and inf[2]>0:
    n1 = inf[2] * -1
    inf[2] = n1
elif  
print('-='*20)
print(f'{inf},{inf[0]},{inf[1]},{inf[2]}')
for c in range(inf[0],inf[1],inf[2]):
    print(f'{c}',end=' ',flush = True)
    sleep(0.5)
