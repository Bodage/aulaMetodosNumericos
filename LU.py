from sympy import *

def main():
    squareM = [[5, 2, 1],
               [3, 1, 4],
               [1, 1, 3]]
    solM = [[0],
            [-7],
            [-5]]

    retLU = LU(squareM)
    if retLU[0] != 1:
        print(retLU[1])
        return
    else:
        print(f'L = {retLU[2][0]}\n')
        print(f'U = {retLU[2][1]}\n')
                
def LU(m):
    n = len(m)

    L = [[0 for _ in range(n)] for _ in range(n)]
    U = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        L[i][i] = 1

    for i in range(n):
        for j in range(i, n):
            soma = 0
            for k in range(i):
                soma += L[i][k]*U[k][j]
            
            U[i][j] = m[i][j]-soma
        
        for j in range(i+1, n):
            soma = 0
            for k in range(i):
                soma += L[j][k]*U[k][i]
            
            if U[i][i] == 0:
                return [0, 'Pivo 0']

            L[j][i] = (m[j][i]-soma)/U[i][i]
    
    return [1, '', [L, U]]

if __name__ == '__main__':
    main()