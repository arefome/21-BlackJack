import random


def baraja():
    return [(n, p) for n in ['A', 'J', 'Q', 'K'] +
            [str(x) for x in range(2, 11)]for p in ['♠', '♡', '♢', '♣']]


def mezclar(baraja):
    random.shuffle(baraja)
    return baraja


def valor_carta(carta):
    if carta[0] in ['J', 'Q', 'K']:
        return 10
    elif carta[0] == 'A':
        return 1
    else:
        return int(carta[0])


def valor_mano(mano):
    if mano == []:
        return 0
    return valor_carta(mano[0]) + valor_mano(mano[1:])


def valor_mano_recargado(mano):
    if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
        return valor_mano(mano) + 10
    else:
        return valor_mano(mano)


def sacar_carta(mazo, mano):
    if mazo == []:
        return mano
    return mano + [mazo[0]]


def jugar(mazo, mano_jugador, mano_casa):
    while len(mano_jugador) < 2:
        jugar(mazo[2:], mano_jugador + [mazo[0]], mano_casa + [mazo[1]])

    if (valor_mano_recargado(mano_jugador) >= 21
            or valor_mano_recargado(mano_casa) >= 21):
        validar_ganador(mano_jugador, mano_casa)
    else:
        print('mano Jugador: ', valor_mano_recargado(mano_jugador))
        mostrar_mano(mano_jugador)
        print('mano casa: ')
        mostrar_mano_oculta(mano_casa)

        if not pedir_carta():
            validar_ganador(mano_jugador, juego_casa(mazo[2:], 
                            mano_jugador, mano_casa))

    jugar(mazo[2:], mano_jugador + [mazo[0]], mano_casa)


def juego_casa(mazo, mano_jugador, mano_casa):
    if valor_mano_recargado(mano_jugador) <= valor_mano_recargado(mano_casa):
        return mano_casa
    return juego_casa(mazo[1:], mano_jugador, sacar_carta(mazo, mano_casa))


def pedir_carta():
    return True if input('''¿Carta?:\n [s]i\n [n]o\n...''') == 's' else False


def continuar():
    input('Presione una tecla para continuar...')
    print("------- NUEVO JUEGO ---------")
    jugar(mezclar(baraja()), [], [])


def validar_ganador(mano_jugador, mano_casa):
    print('Evaluando ganador...')
    print('mano Jugador: ', valor_mano_recargado(mano_jugador))
    mostrar_mano(mano_jugador)
    print('mano casa: ', valor_mano_recargado(mano_casa))
    mostrar_mano(mano_casa)

    if ((valor_mano_recargado(mano_casa) >= valor_mano_recargado(mano_jugador)
            or valor_mano_recargado(mano_jugador) > 21)
            and valor_mano_recargado(mano_casa) <= 21):
        print('CASA ha ganado')
    elif ((valor_mano_recargado(mano_jugador) > valor_mano_recargado(mano_casa)
            or valor_mano_recargado(mano_jugador) == 21
            or valor_mano_recargado(mano_casa) > 21) 
            and valor_mano_recargado(mano_jugador) <= 21):
        print('JUGADOR ha ganado')

    continuar()


def mostrar_mano(mano):
    print(' ___    ' * len(mano))
    print(dibujar_top(mano))
    print(dibujar_centro(mano))
    print(dibujar_piso(mano) + '\n')


def mostrar_mano_oculta(mano):
    print(' ___    ' * len(mano))
    print('|   |   ' + dibujar_top(mano[1:]))
    print('|///|   ' + dibujar_centro(mano[1:]))
    print('|___|   ' + dibujar_piso(mano[1:]) + '\n')


def dibujar_top(mano):
    if len(mano) == 1:
        return '|'+mano[0][0]+' |   ' if (mano[0][0] == '10') else '|'+mano[0][0]+'  |   '
    return dibujar_top([mano[0]]) + dibujar_top(mano[1:])


def dibujar_centro(mano):
    if len(mano) == 1:
        return '| '+mano[0][1]+' |   '
    return dibujar_centro([mano[0]]) + dibujar_centro(mano[1:])


def dibujar_piso(mano):
    if len(mano) == 1:
        return '|_'+mano[0][0]+'|   ' if (mano[0][0] == '10') else '|__'+mano[0][0]+'|   '
    return dibujar_piso([mano[0]]) + dibujar_piso(mano[1:])


jugar(mezclar(baraja()), [], [])
