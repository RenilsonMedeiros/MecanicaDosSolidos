# Cálculo das componentes das tensões aplicadas em um corpo 
# sujeito a um estado plano de tensões

import matplotlib.pyplot as plt
import numpy as np
import math as mt

#Defina os valores das tensões normais e da tensão cisalhante para o plano dado
sigma_x = 50
sigma_y = -10
tau_xy = 40


#CALCULANDO E PLOTANDO O CÍRCULO DE MOHR
sigma_m = round((sigma_x + sigma_y)/2, 3)
R=round(np.sqrt(((sigma_x - sigma_y)/2)**2 + tau_xy**2), 3)

draw_circle = plt.Circle((sigma_m,0), R, fill=False)

figure, axes = plt.subplots()

figure = plt.gcf()
axes = plt.gca()
axes.cla()

offset = 10
xlim_inf = sigma_m - R - offset
xlim_sup = sigma_m + R + offset
ylim_inf =  - R - offset
ylim_sup = + R + offset

axes.set_xlim((xlim_inf,xlim_sup))
axes.set_ylim((ylim_inf,ylim_sup))

ofs = 3
str_sigma_x = '('+str(sigma_x)+','+str(tau_xy)+')'
axes.annotate(str_sigma_x, (sigma_x,tau_xy),(sigma_x+ofs,tau_xy+ofs), color='green')
axes.plot((sigma_x),(tau_xy),'o',color='green')

str_sigma_y = '('+str(sigma_y)+','+str(-tau_xy)+')'
axes.annotate(str_sigma_y, (sigma_y,-tau_xy),(sigma_y+ofs,-tau_xy+ofs), color='green')
axes.plot((sigma_y),(-tau_xy),'o',color='green')

str_tauMax1 = '('+str(sigma_m)+','+str(R)+')'
axes.annotate(str_tauMax1, (sigma_m,R),(sigma_m+ofs,R+ofs), color='red')
axes.plot((sigma_m),(R),'o',color='red')

str_tauMax2 = '('+str(sigma_m)+','+str(-R)+')'
axes.annotate(str_tauMax2, (sigma_m,-R),(sigma_m+ofs,-R-2*ofs), color='red')
axes.plot((sigma_m),(-R),'o',color='red')

str_sigmaMax1 = '('+str(round(sigma_m-R, 3))+','+str(0)+')'
axes.annotate(str_sigmaMax1, (sigma_m-R,0),(sigma_m-R+ofs,-2*ofs), color='b')
axes.plot((sigma_m-R),(0),'o',color='b')

str_sigmaMax2 = '('+str(round(sigma_m+R,3))+','+str(0)+')'
axes.annotate(str_sigmaMax2, (sigma_m+R,0),(sigma_m+R-7*ofs,-2*ofs), color='b')
axes.plot((sigma_m+R),(0),'o',color='b')



axes.set_aspect(1)
axes.add_artist(draw_circle)
plt.title('Mohr\'s Circle'+r' $\tau$'+' X $\sigma$', fontsize=18)

plt.show()

#------------ MAIS ALGUMAS INFORMAÇÕES ----------------#

# O plano onde ocorre tensão normal extrema é
rad_thetaP = round((1/2)*mt.atan((2*tau_xy)/(sigma_x-sigma_y)), 3)
deg_thetaP = round(mt.degrees(rad_thetaP), 3)
print('O plano onde ocorre tensão normal extrema é: ')
print(str(rad_thetaP) + 'rad')
print(str(deg_thetaP) + '°')

#O plano onde ocorre tensão cisalhante extrema é
rad_thetaC = round((1/2)*mt.atan(-(sigma_x-sigma_y)/(2*tau_xy)), 3)
deg_thetaC = round(mt.degrees(rad_thetaC), 3)
print('')
print('O plano onde ocorre tensão cisalhante extrema é: ')
print(str(rad_thetaC) + 'rad')
print(str(deg_thetaC) + '°')

