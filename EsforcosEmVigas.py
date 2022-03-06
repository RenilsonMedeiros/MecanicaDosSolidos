import numpy as np
import matplotlib.pyplot as plt

l = 10      #Comprimento da viga
w = -100    #Carregamento distribuido
F = -400    #Força concentrada
R1 = 200    #Reação de apoio 1
R2 = 400    #Reação de apoio 2
 
_loads = ['fc','cd','cd','fc','fc']
_magFc = [R1, R2, F]
_magCd = [w,-w]
_dimFc = [0, 7, 10]
_dimCd = [0, 4]

x = 0
i = 0
V = np.zeros(100*l + 1)
X = np.zeros(100*l + 1)
v1 = np.zeros(2)
x1 = np.zeros(2)

n1 = 0
n2 = 0
n3 = 0
n4 = 0


# DIGRAMA DE ESFORÇO CORTANTE - DEF
for loads in _loads:
  #FUNÇÃO IMPULSO
  if loads is 'mc':
    while (x <= l):
      if (abs(x - _dimM[n1]) < 0.0001): V[i] = V[i] + 0
      else: V[i] = V[i] + 0
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n1 = n1 + 1

  #FUNÇÃO DEGRAU
  if loads is 'fc':
    while (x <= l):
      X[i] = x
      if (x < _dimFc[n2]): V[i] = V[i] + 0
      else: V[i] = V[i] + _magFc[n2]
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n2 = n2 + 1
  
  #FUNÇÃO RAMPA
  if loads is 'cd':
    while (x <= l):
      if (x < _dimCd[n3]): V[i] = V[i] + 0
      else: V[i] = V[i] + _magCd[n3]*(x - _dimCd[n3])
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n3 = n3 + 1

  #FUNÇÃO QUADRÁTICA
  if loads is 'ct':
    while (x <= l):
      if (x < _dimCt[n4]): V[i] = V[i] + 0
      else: V[i] = V[i] + ((_magCt[n4])/(2*_tamCt[n4]))*((x - _dimCt[n4])**2)
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n4 = n4 + 1

plt.plot(X, V)
plt.show()

V = np.zeros(100*l + 1)
n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

#DIAGRAMA DE MOMENTO FLETOR - DMF
for loads in _loads:
  #FUNÇÃO IMPULSO
  if loads is 'u':
    while (x <= l):
      if (abs(x - _dimU[n1]) < 0.0001): V[i] = V[i] + 0
      else: V[i] = V[i] + 0
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n1 = n1 + 1

  #FUNÇÃO DEGRAU
  if loads is 'mc':
    while (x <= l):
      X[i] = x
      if (x < _dimM[n2]): V[i] = V[i] + 0
      else: V[i] = V[i] + _magM[n2]
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n2 = n2 + 1
  
  #FUNÇÃO RAMPA
  if loads is 'fc':
    while (x <= l):
      if (x < _dimFc[n3]): V[i] = V[i] + 0
      else: V[i] = V[i] + _magFc[n3]*(x - _dimFc[n3])
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n3 = n3 + 1

  #FUNÇÃO QUADRÁTICA
  if loads is 'cd':
    while (x <= l):
      if (x < _dimCd[n4]): V[i] = V[i] + 0
      else: V[i] = V[i] + ((_magCd[n4])/2)*((x - _dimCd[n4])**2)
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n4 = n4 + 1

  #FUNÇÃO CÚBICA
  if loads is 'ct':
    while (x <= l):
      if (x < _dimCt[n5]): V[i] = V[i] + 0
      else: V[i] = V[i] + ((_magCt[n5])/(6*_tamCt[n5]))*((x - _dimCt[n5])**3)
      i = i + 1
      x=round(x+0.01,2)
    i = 0
    x = 0
    n5 = n5 + 1

plt.plot(X, V)
plt.show()

#Feche o primeiro gráfico que surgir para plotar o 2º gráfico.