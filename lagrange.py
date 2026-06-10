from sympy import *

def main():
    xs = [-1, 0, 3]
    fxs = [15, 8, -1]

    print(lagrange(xs, fxs))

def lagrange(xs, fxs):
    x = symbols('x')

    sum = 0
    for i in range(len(fxs)):
        num = 1
        den = 1
        for j in range(len(xs)):
            if i == j:
                continue
            num *= (x-xs[j])
            den *= (xs[i]-xs[j])
        
        sum += fxs[i]*num/den
    
    return expand(sum)

if __name__ == '__main__':
    main()