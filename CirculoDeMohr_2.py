# Cálculo das componentes das tensões aplicadas em um corpo 
# sujeito a um estado plano de tensões

# USE ESSE SCRIPT SE:
# Quiseres saber qual a tensão normal e cisalhante em qualquer 
# plano da estrutura conhecendo apenas o ângulo que esse plano 
# forma com o eixo y, use as expressões abaixo.

import math as mt

#Defina os valores das tensões normais e da tensão cisalhante e o ângulo para o plano dado
theta = 10
sigma_x = 50
sigma_y = -10
tau_xy = 40

# Descomente a linha abaixo caso o ângulo informado esteja em graus
# theta = mt.radians(theta)

sig_X = round((sigma_x+sigma_y)/2 + ((sigma_x-sigma_y)/2)*mt.cos(2*theta) + tau_xy*mt.sin(2*theta), 3)
sig_Y = round((sigma_x+sigma_y)/2 - ((sigma_x-sigma_y)/2)*mt.cos(2*theta) - tau_xy*mt.sin(2*theta), 3)
tau_XY = round(-((sigma_x-sigma_y)/2)*mt.sin(2*theta) + tau_xy*mt.cos(2*theta), 3)

print('Segue a ordem: Sigma_x, Sigma_y e tau_xy nesse plano:')
print(sig_X)
print(sig_Y)
print(tau_XY)

# Checagem de invariância das tensões no respectivo plano
if((sig_X + sig_Y) == (sigma_x + sigma_y)): print('esse plano de tensões é TOTALMENTE POSSÍVEL')
else: print('esse plano de tensões é IMPOSSÍVEL DE EXISTIR')