from sympy import *

def main():
    x = symbols('x')

    precision = 0.001
    funct = x**2+2*x-5
    tries = 1000
    guess = [1, 5]

    for i in range(len(guess)//2):
        intervalo = guess[i*2:i*2+2]
        print(f'{intervalo}:\n{secante(intervalo, funct, tries, precision)}')

def secante(guess, funct, tries, prec):
    x = symbols('x')

    retVGuess = validarGuess(guess)
    if retVGuess[0] != 1:
        return retVGuess[1]
    else:
        guess = retVGuess[2]

    side = True
    ys = [funct.subs(x, guess[0]), prec]

    if abs(ys[0]) < prec or abs(ys[1]) < prec:
        return f'Um dos chutes da 0\nguess[0] = {guess[0]} = {ys[0]}\nguess[1] = {guess[1]} = {ys[1]}'

    for i in range(tries):
        ys[side] = funct.subs(x, guess[side])

        if abs(ys[side]) < prec:
            return f'f(x) = f({guess[side]}) = {ys[side]}, ' + '{' + f'|f(x)| < {prec}' + '}' + f'({i} tentativas)'
        
        if i == tries-1:
            break

        side = not side
        guess[side] = (guess[side]*ys[not side]-guess[not side]*ys[side])/(ys[not side]-ys[side])
    return f'f(x) = 0 não achado em {tries} tentativas\nUltimo achado é f({guess[side]}) = {ys[side]}'

def validarGuess(guess):
    if guess[0] == guess[1]:
        return [0, f'chutes tem o mesmo valor\nguess[0] = {guess[0]}\nguess[1] = {guess[1]}']
    if guess[0] > guess[1]:
        return [1, '', [guess[1], guess[0]]]
    else:
        return [1, '', guess]

if __name__ == '__main__':
    main()