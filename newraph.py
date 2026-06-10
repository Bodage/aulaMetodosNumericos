from sympy import *

def main():
    x = symbols('x')

    precision = 0.001
    funct = x**2+2*x-5
    tries = 1000
    guess = [3]

    for i in range(len(guess)):
        print(f'[{i}]:\n{newraph(guess[i], funct, tries, precision)}')

def newraph(guess, funct, tries, prec):
    x = symbols('x')
    dy = diff(funct)

    newX = guess
    y = 0
    for i in range(tries):
        y = funct.subs(x, newX)

        if abs(y) < prec:
            return f'f(x) = f({newX}) = {y}, ' + '{' + f'|f(x)| < {prec}' + '}' + f'({i} tentativas)'
        
        newX = newX - y/dy.subs(x, newX)
    return f'f(x) = 0 não achado em {tries} tentativas\nUltimo achado é f({newX}) = {y}'

if __name__ == '__main__':
    main()