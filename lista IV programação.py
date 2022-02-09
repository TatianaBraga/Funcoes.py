# 1) Faça uma função que receba, por parâmetro, 3 valores inteiros positivos k, m e n (k < m < n) e imprima todos os múltiplos de k no intervalo [m, n].
#(Ex: k = 3, m = 20, n = 30 → 21, 24, 27, 30).
'''
def lista(k,m,n):
    fim = int(input('Digite um número inteiro(fim): '))
    inicio = int(input('Digite um número inteiro(inicio): '))
    passo = int(input('Digite um número inteiro(passo): '))
    for x in range (m,n+1,k):
        if x%k ==0:
            print(f'{x} é múltiplo de {k}')
fim = int(input('Digite um número inteiro(fim): '))
inicio = int(input('Digite um número inteiro(inicio): '))
passo = int(input('Digite um número inteiro(passo): '))
lista(passo,inicio,fim)
'''
''' 
def mult(k,m,n):
    for x in range(m,n+1,k):
        if x%k==0:
            print(x)
        else:
            break      
x = int(input('Digite o menor valor inteiro: '))
y = int(input('Digite o valor inteiro intermediário: '))
z = int(input('Digite o maior valor inteiro: '))
mult(x,y,z)
'''

# 2) Faça uma função que receba, por parâmetros, dois
#valores inteiros positivos X e Y e que calcule XY,
#sem utilizar o operador de potência (utilize a definição: XY = X × X × · · · × X | {z }
#Y vezes).
'''
def potência (x,y):
    return x*y
    print("Soma: ",somatorio(x,y) )
c = float(input('Digite um valor real: '))
d = float(input('Digite um número real:'))
e = potência(c,d)
print(e)
'''


# 3) Faça uma função que receba, por parâmetro, um
#valor real x e arrendonde esse número para o inteiro mais próximo. Para valores como 2, 5 e 5, 5
#arredonde para o par mais próximo: 2, 5 ⇒ 2; 5, 5 ⇒ 6.
'''
def arredonde (x):
    y = x
    z = round(y)
    print(f'{z}')
b = float(input('Digite um número: '))
r = arredonde(b)
'''
# 4)
'''
def sequencia(k):
    
    an = ((((-1)**k)*(k + 1))/3**k)
    print(an)
x = int(input('Digite um número inteiro: '))
r = sequencia(x)
'''

# 5) Faça uma função que receba, por parâmetros, seis valores reais,n1,n2,n3,n4,n5en6, e retorne o menor deles
# (sugestão: faça antes, primeiramente,uma função que calcule o menor entre 2 números,depois uma função que calcule o menor entre 3 números)
'''
def menor2(x,y):
    return x if x < y else y
def menor3(x,y,z):
    if x < y and x < z:
        return x
    elif y < x and y < z:
        return y
    elif z < x and z < x:
        return z
def menor6 (x,y,z,w,i,j):
    r1 = menor3(x,y,z)
    r2 = menor3(w,i,j)
    return menor2(r1,r2)
e1 = float(input('digite o valor 1: '))
e2 = float(input('digite o valor 2: '))
e3 = float(input('digite o valor 3: '))
e4 = float(input('digite o valor 4: '))
e5 = float(input('digite o valor 5: '))
e6 = float(input('digite o valor 6: '))
menor = menor6(e1,e2,e3,e4,e5,e6)
print(f'{menor}')

'''


# 6) Faça uma função que receba, por parâmetros, quatro valores reais positivos, n1, n2, n3 e n4, e retorne
# a média aritmética entre o maior e o menor deles.
'''
def mediaArit(n1,n2):
    return n1 if n1 < n2 else n2

def mediaAriti(n3,n4):
    return n3 if n3 < n4 else n4

def mediaAritmetica(n1,n2,n3,n4):
    w1 = mediaArit(n1,n2)
    w2 = mediaArit(n3,n4)
    return mediaAriti(w1,w2)

def mediaAita(s1,s2):
    return s1 if s1 > s2 else s2

def mediaAitac(s3,s4):
    return s3 if s3 > s4 else s4

def mediaAritmetic(s1,s2,s3,s4):
    h1 = mediaAita(s1,s2)
    h2 = mediaAita(s3,s4)
    return mediaAitac(h1,h2)
f1 = float(input('digite o valor 1: '))
f2 = float(input('digite o valor 2: '))
f3 = float(input('digite o valor 3: '))
f4 = float(input('digite o valor 4: '))
menor = mediaAritmetica(f1,f2,f3,f4)
maior = mediaAritmetic(f1,f2,f3,f4)
print(menor)
print(maior)
print(f'{(menor + maior)/2}')

'''
# 7) Faça uma função que receba, por parâmetro, um valor inteiro positivo n e imprima todos os divisores
# naturais desse número.
'''
n = int(input('Digite um inteiro: '))
def divisor(n):
    for x in range(1,n+1):
        if n%x == 0:
            print(x)
        
        
g = divisor(n)
print(g)
'''

# 8) Faça uma função que receba, por parâmetro, dois
# valores inteiros positivos a e b e retorne o Máximo
# Divisor Comum (mdc) entre eles. Sugestão: Utilize
# o algoritmo de Euclides.
'''
def mdc(a,b):
    rt = a%b
    while rt !=0:
        a = b
        b = rt
        rt = a%b
    return b
h = int(input('Digite o primeiro número inteiro positivo: '))
k = int(input('Digite o segundo número inteiro positivo: '))
MDC = mdc(h,k)
print(f'O MDC de {h} e {k} é  igual {MDC}')

'''

# 9) Faça uma função que receba, por parâmetro, dois
# valores inteiros positivos a e b e retorne o Mínimo
# Múltiplo Comum (mmc) entre eles. Sugestão: Utilize a relação

'''
def MDC(a,b):
    rt = a%b
    while rt != 0:
        a = b
        b = rt
        rt = a%b
    return b
def MMC (a,b):
    mdc = MDC(a,b)
    return a*b//mdc
x = int (input('Digite o valor para o primeiro parâmetro: '))
y = int(input('Digite o valor para o segundo parâmetro: '))
mmc = MMC(x,y)
print(f'O MMC de {x} e {y} é igual a {mmc}')

'''
# 10) sequência de Padovan [...]Faça uma função que receba, por parâmetro, um
#valor inteiro positivo n, calcule e retorne o n-ésimo
#termo da sequência de Padovan.
'''
def padovan (n):
    
'''
# 11) Faça uma função que receba, por parâmetro, um
# valor inteiro positivo n e retorne sua quantidade de
# dígitos (Ex: n = 581 → 3).

'''
def quantificador (n):
    f = 0
    while n > 0:
        n //= 10
        f += 1
    return f
x = int(input('Digite um valor: '))
w = quantificador (x)
print(f'A quantidade de dígitos de {x} é {w}')

'''
#12) Faça uma função que receba, por parâmetro, um
# valor inteiro positivo n e retorne a soma dos seus
# dígitos (Ex: n = 3472 → 3 + 4 + 7 + 2 = 16).

'''
def somadig(n):
    f = 0
    while n > 0:
        n //= 10
        f +=%10
    return f
p = int(input('Digite um valor: '))
h = somadig(p)
print(f'A soma é igual: {h}')

'''
#13) Faça uma função que receba, por parâmetro, um
#valor inteiro positivo n e retorne seu maior dígito
#(Ex: n = 3472 → 7).
'''
def maior(n):
    f = 0
    while n > 0:
        if n %10> f:
            f = n%10
        n//=10
    return f
i = int(input('Digite um valor inteiro: '))
g = maior(i)
print(g)
'''
# 14) Faça uma função que receba, por parâmetro, um
# valor inteiro positivo n e inverta a ordem dos seus
# dígitos (Ex: n = 3482 → 2843).
'''
def ordem(n):
    f = 0
    while n > 0:
        f = f*10 + n%10
        n //= 10
    return f
c = int(input('Digite um valor inteiro: '))
s = ordem(c)
print(s)
'''

# 15) Faça uma função que receba, por parâmetro, um valor inteiro positivo n e que verifique se este número
# é um palíndromo. A função deve retornar True ou
# False. (Ex: n = 259952 → True).
'''
def inverter(n):
    g = 0
    while n > 0:
        g = g*10 + n%10
        n//=10
    return g
def Palíndromo(n): 
    x = inverter(n) 
    return n == x
t = int(input('Digite um valor inteiro: '))
l = Palíndromo(t)
print(l)
'''

# 16) Faça uma função que receba, por parâmetro, um
# valor inteiro positivo n e adicione uma unidade a
# todos os seus dígitos (Ex: n = 3412 → 4523). Considere 9 + 1 = 0 (Ex: n = 491 → 502).
'''
def inverter(n):
    d = 0
    while n > 0:
        d = d*10 + n%10
        n//=10
    return d
def inverternovamente(n):
    d = 0
    while n > 0:
        d = d*10 + n%10
        n//=10
    return d
def soma(n):
    c = inverter (n)
    return  c+1
f = int(input('Digite um valor: '))
s = soma(f)
print(s)

'''

# 17) Faça uma função que receba, por parâmetro, um
# valor inteiro positivo n e exiba (imprima na tela)
# todos os números primos menores que n.
'''
def primo(x):
    for u in range(2,x):
        if x%u ==0:
            return False
    return True
def imprimir(n):
    for i in range(2,n+1):
        if primo(x):
            print(x)
n = int(input('Digite um valor inteiro: '))
imprimir(n)


'''
def Primo(x): # x = 13
    for i in range(2,x): # i = 2 (2,3,...11,12)
        if x%i == 0:
            return False
    return True
def ImprimePrimo(n): # n = 7
    for x in range(2,n+1): # x = 2 (2,3,4,5,6,7)
        if Primo(x):
            print(x)
n = int(input('Valor inteiro positivo: ')) # n = 7
ImprimePrimo(n)


# 18) Faça uma função que receba, por parâmetro, um valor inteiro positivo n e que verifique se este número é
# triangular. A função deve retornar True ou False.
# Obs: Um número é triangular quando é o resultado
# do produto de 3 números naturais consecutivos (Ex:
# 24 = 2 × 3 × 4).
'''
def Triangular(n): # n = 60
    x = 1
    t  = 6 
    while t <= n:
        if t == n:
            return True
        x += 1                   # x = 3
        t   = x*(x+1)*(x+2) # t = 60
    return False
n = int(input('Valor inteiro positivo: ')) # n = 60
r = Triangular(n)                                 # r = True
print(f'Triangular? -> {r}')
'''


