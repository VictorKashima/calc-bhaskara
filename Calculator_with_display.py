import PySimpleGUI as pg

#TEMA
pg.theme('DarkPurple4')

#LAYOUT
layout = [
        [
            pg.Text('Valor de "a"', font='Arial 15'), 
            pg.Input(key='valora')
        ],
        [
            pg.Text('Valor de "b"', font='Arial 15'), 
            pg.Input(key='valorb')
        ],
        [
            pg.Text('Valor de "c"', font='Arial 15'), 
            pg.Input(key='valorc')
        ],
        [
            pg.Text('Resultado:', font='Arial 15'), 
            pg.Radio('Delta', 'grupo 1', key='delta'),
            pg.Radio('"x1" e "x2"', 'grupo 1', key='x1x2'), 
            pg.Radio('Tudo', 'grupo 1', key='all')
        ],
        [
            pg.Button('Calcular'), pg.Button('Cancelar')
        ]
    ]

#JANELA
janela = pg.Window('Calculadora Bhaskara', layout)

#LOOP DE EVENTOS
while True:
    evento, valor = janela.read()
    if evento == "Cancelar" or evento == pg.WIN_CLOSED:
        break
    elif evento == "Calcular":
        print(f"Valor A: {valor['valora']}")
        print(f"Valor B: {valor['valorb']}")
        print(f"Valor C: {valor['valorc']}")
        if valor['delta'] == True:
            print(f"Delta")
        if valor['x1x2'] == True:
            print(f"x1x2")
        if valor['all'] == True:
            print(f"all")

#FECHAR A JANELA
janela.close()
exit()