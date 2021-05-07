dados = dict()
gols = list()
dados['nome'] = str(input('Nome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
dados['gols'] = gols
dados['total'] = sum(gols)
print('=' * 45)
print(dados)
print('=' * 45)
for k, v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('=' * 45)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'   =>> Na partida {c + 1}, ele fez {gols[c]} gol(s).')
print(f'Foi um total de {dados["total"]} gols.')
