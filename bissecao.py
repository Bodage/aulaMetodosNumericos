import os
import decimal
from sympy import *
import math

def main() -> None:
    x = symbols('x')
    
    precision = 0.001
    funct = x**2-2*x-5
    tries = 1000
    guess = [0, 4]

    for i in range(len(guess)//2):
        intervalo = guess[i*2:i*2+2]
        print(f'{intervalo}:\n{bissecao(precision, funct, tries, intervalo)}\n')

def bissecao(precisao:float, funct:any, tries:int, guess:list = [None, None]) -> str:
    x = symbols('x')
    prec = [0-precisao, precisao]
    
    retVGuess = validaGuess(guess, funct)
    if retVGuess[0] != 1:
        return retVGuess[1]
    else:
        guess = retVGuess[2]
        newg = 0
        y = 0
        for i in range(tries):
            newG = (guess[0]+guess[1])/2
            y = funct.subs(x ,newG)
            if y > prec[0] and y < prec[1]:
                return f'f({newG}) = {y}, ' + '{' + f'|f(x)| < {precisao}' + '}' + f'({i} tentativas)'
            elif y > 0:
                guess[1] = newG
            else:
                guess[0] = newG
        return f'f(x) = 0 não achado em {tries} tentativas\nUltimo achado é f({newg}) = {y}'
        
def validaGuess(guess:list, funct:any) -> list:
    if guess[0] == guess[1]:
        return [1, 'guess[0] não pode ser igual à guess[1]']
    x = symbols('x')
    msg = ''
    mult = 1
    yn = 0
    for i in range(len(guess)):
        yn = funct.subs(x, guess[i])
        mult *= yn
        msg += f'\nf(x{i}) = f({guess[i]}) = {yn}'
    if mult < 0:
        over = guess[1] if yn > 0 else guess[0]
        lower = guess[0] if over == guess[1] else guess[1]
        return [1, '', [lower, over]]
    if mult > 0:
        msg = 'Os chutes são ambos positivos/negativos' + msg
        return [0, msg]
    if mult == 0:
        msg = 'O f(x) de algum dos chutes é 0' + msg
        return [-1, msg]

if __name__ == '__main__':
    main()
    