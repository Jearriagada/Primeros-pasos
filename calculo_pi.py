import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size

n = 1000000000 #número de observaciones

x = np.random.uniform( #distribución aleatoria en eje x
                low=-1,
                high=1, 
                size=[ n,1 ]
                )
y = np.random.uniform( #distribución aleatoria en eje y
                low=-1,
                high=1, 
                size=[ n,1 ]
                )

crl = x**2+y**2 <1 #área dentro del círculo
pi = np.sum(crl)*4/n

# x_in = x[ crl ] #filtrar coordenadas dentro del círculo
# y_in = y[ crl ] #filtrar coordenadas dentro del círculo

# plt.figure(
#             figsize=[ 5,5 ]
#             )
# plt.scatter(
#             x, y, s=1                  #tamaño cuadrado
#             )
# plt.scatter(
#             x_in, y_in, color='r', s=1 #tamaño círculo
#             )
# plt.title(
#             (f"pi: {round(np.pi,8)}, aproximación: {pi}") #muestra de datos
#             ) 
# plt.show()

print(
        f"pi: {np.pi}, aproximación: {pi}" #muestra de datos
        ) 
