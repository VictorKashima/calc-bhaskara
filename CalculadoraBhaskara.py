#Calculadora de equação do 2° grau

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

print('-'*50)
print('{}CALCULADORA BHASKARA{}' .format(color.BOLD, color.END) )
print('-'*50)

print('obs* o valor de A é aquele que acompanha o x²')
a = int(input('{}Digite o valor de A:{}' .format(color.BOLD, color.END)))
print('- '*25)

print('obs* o valor de B é aquele que acompanha o x')
b = int(input('{}Digite o valor de B:{}' .format(color.BOLD, color.END)))
print('- '*25)

print('obs* o valor de C é aquele que não acompanha nenhuma incógnita')
c = int(input('{}Digita o valor de C:{}' .format(color.BOLD, color.END)))
print('- '*25)

print('. . . Calculando . . .')
print('- '*25)

#Realizando o cálculo
#Equação de delta
d = ((b**2)-4*a*c)
#Raíz quadrada de delta
r = (d**(1/2))
#Primeira solução
x1 = ((-b)+r)/(2*a)
#Segunda solução
x2 = ((-b)-r)/(2*a)

#FUNCIONA DESGRAÇA

print('Aqui estão os resultados:')
print('-'*50)
print('Valor de Delta Δ: {}{}{}' .format(color.BOLD, d, color.END))
print('-'*50)
print('obs* O valor de x1 é a parte da soma e o x2 é da subtração')
print('Valor de x1: {}{}{}' .format(color.BOLD, x1, color.END))
print('Valor de x2: {}{}{}' .format(color.BOLD, x2, color.END))
print('-'*50)
