def ficha(nome='', gols=''):
    if '' == nome and gols == '':
        return 'O jogador <Desconhecido> fez 0 gol(s) no campeonato'
    elif nome == '':
        return f'O jogador <Desconhecido> fez {gols} gol(s) no campeonato.'
    elif gols == '':
        return f'O jogador {nome} fez 0 gol(s) no campeonato.'
    else:
        return f'O jogador {nome} fez {gols} gol(s) no campeonato.'


print(ficha(str(input('Nome do jogador: ')).strip(), str(input('Numero de gols: ')).strip()))
