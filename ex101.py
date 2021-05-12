def voto(ano):
    from datetime import datetime
    atual = datetime.now().year
    idade = atual - ano
    if 16 <= idade <= 17 or idade > 60:
        return idade, 'VOTO OPCIONAL!'
    elif 18 <= idade < 60:
        return idade, 'VOTO OBRIGATÓRIO!'
    else:
        return idade, 'NÃO VOTA!'


nas = int(input('Em que ano voce nasceu? '))
print(f'Com {voto(nas)[0]} anos: {voto(nas)[1]}')
