dados = dict()
gols = list()
time = list()
while True:
    dados['nome'] = str(input('Nome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    dados['gols'] = gols[:]
    dados['total'] = sum(gols)
    time.append(dados.copy())
    dados.clear()
    gols.clear()
    op = str(input('Deseja digitar dados de outro jogador [S/N]? ')).strip()[0]
    if op in 'Nn':
        break
    print('-' * 46)
print('=' * 46, '\n', end='nº   ')
for k in time[0].keys():
    print(f'{k :<14}   ', end='')
print()
print('-' * 46)
for c in range(0, len(time)):
    print(f'{c + 1 :<5}', end='')
    for d in time[c].values():
        print(f'{str(d) :<17}', end='')
    print()
print('=' * 46)
d = int(input('Deseja saber os dados de qual jogador[999/sair]: '))
while True:
    print(f'O jogador {time[d - 1]["nome"]} jogou {len(time[d - 1]["gols"])} partidas:')
    for c in range(0, len(time[d - 1]["gols"])):
        print(f'  => Na partida {c + 1} ele fez {time[d - 1]["gols"][c]}.')
    print(f'  => Um total de {time[d - 1]["total"]} gols.')
    d = int(input('Deseja saber os dados de qual jogador[999/sair]: '))
    if d == 999:
        break
    print('=' * 46)
