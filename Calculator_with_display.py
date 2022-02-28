import PySimpleGUI as pg

#TEMA
pg.theme('DarkPurple4')

#MENU
menu_layout = [
    ['Ajuda', ['Como funciona', 'O que é Bhaskara', 'Como usar']],
    ['Doação', ['PIX', 'PayPal', 'Boleto', 'Endereço', 'Caixa Postal', 'Conta Bancária']]
]

#LAYOUT
layout = [
        [pg.Menu(menu_layout)],
        [
            pg.Text('Valor de "a"', font='Arial 15'), 
            pg.Input(key='a')
        ],
        [
            pg.Text('Valor de "b"', font='Arial 15'), 
            pg.Input(key='b')
        ],
        [
            pg.Text('Valor de "c"', font='Arial 15'), 
            pg.Input(key='c')
        ],
        [
            pg.Text('Resultado:', font='Arial 15'), 
            pg.Radio('Delta', 'grupo 1', key='d'),
            pg.Radio('"x1" e "x2"', 'grupo 1', key='x1x2'), 
            pg.Radio('Tudo', 'grupo 1', key='all')
        ],
        [
            pg.Button('Calcular'), pg.Button('Cancelar')
        ]
    ]

#JANELA
WIN_W = 30
WIN_H = 50

class App():
    def _init_(self):
        self.window = pg.Window('Calculadora Bhaskara', layout=layout, margins=(0, 0), resizable=True)
        self.result = 0
        self.window.read(timeout=3)
    for i in range(1, 3):
        for button in layout[i]:
            button.expand(expand_x=True, expand_y=True)
    
    #FUNÇÕES MENU
    def comofunciona(self):
        pg.popup('Como Funciona', 'Você insere os valores respectivos a cada letra e o programa realiza o cálculo e entrega os valores de delta, x1 e x2.')

    #INICIAR O PROGRAMA
    def start(self):
        while True:
            evento, self.values = self.window.read()

            if evento in (None, 'Cancelar', pg.WIN_CLOSED):
                break

            if event in ('comofunciona'):
                self.comofunciona()