# serie = []
# for i in range(1000000):
#     serie.append((1/((i+1)**2)))
# basilea = sum(serie)
# print((basilea*6)**(1/2))

seed = 2.5

def corrmatrix(n,seed):
          
    np.random.seed(seed)
    b = np.random.uniform(-1,1, size=[n,n])
    m = np.tril(b) + np.tril(b, -1).T

    for i in range(n):
        for j in range(n):
            if i == j:
                m[i,j]=1      

    return print(m)
