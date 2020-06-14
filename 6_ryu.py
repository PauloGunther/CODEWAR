# SOMA DOS DIVISIVEIS POR 5 E 3
def numero(num):
    s = 0
    for i in range(0, num):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)


# ESCREVER PALAVRAS COM MAIS DE 4 LETRAS AO CONTRARIO
def letra(texto):
    a = str(texto) .split()
    frase = texto
    for i in a:
        if len(i) > 4:
            t = ''
            for n in range(len(i) - 1, -1, -1):
                t = t + i[n]
            frase = str(frase).replace(str(i), str(t))
    print(frase)


# DESLOCAMENTO EM PLANO CARTESIANO VOLTANDO AO MESMO PONTO
def cartesiano(l_main):
    x = {'n': 1, 's': -1}
    y = {'e': 1, 'w': -1}
    lx = []
    for i in l_main:
        if i in 'sn':
            lx.append(x[i])
    ly = []
    for i in l_main:
        if i in 'ew':
            ly.append(y[i])
    if sum(ly) == 0 and sum(lx) == 0 and len(l_main) == 10:
        print(True)
    else:
        print(False)


# CONTANDO NUMERO DE VOGAIS
def vogais(texto):
    c = 0
    for i in str(texto):
        if i in 'aeiou':
            c += 1
    print(c)


# LIKES COMO INSTAGRAM
def likes(a):
    if len(a) == 0:
        print('No one likes this')
    elif len(a) == 1:
        print(f'{a[0]} likes this')
    elif len(a) == 2:
        print(f'{a[0]} and {a[1]} like this')
    elif len(a) == 3:
        print(f'{a[0]}, {a[1]} and {a[2]} like this')
    else:
        print(f'{a[0]}, {a[1]} and {len(a)-2} others like this')


# POSICAO DA LETRA SE REPETIRA
def accum(a):
    f = ''
    for p, i in enumerate(a):
        if p == 0:
            f = str(i * (p + 1)) .title()
        elif (p + 1) < len(a):
            f = f + '-' + str(i * (p + 1)) .title()
        else:
            f = f + '-' + str(i * (p + 1)) .title()
    print(f)