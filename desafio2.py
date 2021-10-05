import numpy as np

def corrmatrix(n,seed=None):
          
    np.random.seed(seed)
    b = np.random.uniform(-1,1, size=[n,n])
    m = np.tril(b) + np.tril(b, -1).T

    for i in range(n):
        for j in range(n):
            if i == j:
                m[i,j]=1      

    return print(m)

corrmatrix(n=6,seed=35089734)


#este código lo hice para transformar el input del seed en float int o none JAJAJAJAJA, no lo quize borrar porque quedó bonito

# def isfloat(seed):
#     try:
#         a = float(seed)
#     except (TypeError, ValueError):
#         return False
#     else:
#         return True

# def isint(seed):
#     try:
#         a = float(seed)
#         b = int(a)
#     except (TypeError, ValueError):
#         return False
#     else:
#         return a == b

# n = int(input(("ingrese el tamaño de la matriz:")))
# seed = input("ingrese una seed: ")

# if isfloat(seed) == False and isint(seed) == False:
#     k1 = None
#     corrmatrix(n,k1)
# elif isfloat(seed) == True and isint(seed) == True:
#     k2 = int(seed)
#     print(k2)
#     corrmatrix(n,k2)
# elif isint(seed) == False and isfloat(seed) == True:
#     k3 = float(seed)
#     k3 = int(k3) #como la funcion seed no acepta float, convertimos el float en un int
#     print(k3)
#     corrmatrix(n,k3)



