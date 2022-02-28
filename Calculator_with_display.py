import PySimpleGUI as pg

#TEMA
pg.theme('DarkPurple4')

#LAYOUT
layout = [
    [pg.Text('Valor de "a"'), pg.Input(key='valora')],
    [pg.Text('Valor de "b"'), pg.Input(key='valorb')],
    [pg.Text('Valor de "c"'), pg.Input(key='valorc')],
    [pg.Button('Calcular'), pg.Button('Cancelar')]
    ]

#JANELA
janela = pg.Window('Calculadora Bhaskara', layout)

#LOOP DE EVENTOS
while True:
    evento, valor = janela.read()
    print(evento)
    print(valor)
    if evento == "Cancelar" or evento == pg.WIN_CLOSED:
        break


#FECHAR A JANELA
janela.close()
exit()