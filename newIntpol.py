from sympy import *

def main():
    nip = NewtonInterpolation()

    i = 0
    while True:
        x = float(input(f'x{i}: ').replace(',','.'))
        fx = float(input(f'f(x{i}): ').replace(',','.'))
        
        nip.add(x, fx)

        print(f'\n{nip}')

class NewtonInterpolation:
    def __init__(self):
        self.pol = ''
        self.x = []
        self.fx = []
        self.cache = []
        self.len = 0
    
    def add(self, x, fx):
        if type(x) == float and type(fx) == float:
            self.len += 1
            self.x.append(x)
            self.fx.append(fx)

        if self.len < 2:
            return
        
        for i in range(1, self.len):
            for j in range(i):
                if j == 1:
                    self.cache.append((self.fx[i]-self.fx[i-1])/(self.x[i]-self.x[i-1]))
                self.cache.append()

        
    def _spnn(self, x):
        return x(x+1)/2
    
    def getFX(self):
        return self.fx

    def getX(self):
        return self.x

    def __str__(self):
        if self.len < 2:
            return 'São necessários pelo menos 2 pontos para gerar um polinômio'
        return self.pol

if __name__ == '__main__':
    main()