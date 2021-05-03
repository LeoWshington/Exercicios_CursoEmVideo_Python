from random import randint
jogadores = dict()
dados = list()
classi = list()
classi2 = list()
pos = 1
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    dados.append(jogadores[f'jogador{c}'])
dados.sort(reverse=True)
classi.append(dados[:])
print(f'Jogador1 tirou {jogadores["jogador1"]} no dado.\n'
      f'Jogador2 tirou {jogadores["jogador2"]} no dado.\n'
      f'Jogador3 tirou {jogadores["jogador3"]} no dado.\n'
      f'Jogador4 tirou {jogadores["jogador4"]} no dado.\n'
      f'{"=" * 30}')
for c in range(0, 4):
    for n in range(0, 4):
        if jogadores[f'jogador{n + 1}'] == classi[0][c] and f'jogador{n + 1}' not in classi2:
            print(f'O {pos}º lugar é jogador{n + 1} com {classi[0][c]} pontos.')
            classi2.append(f'jogador{n + 1}')
            pos += 1
