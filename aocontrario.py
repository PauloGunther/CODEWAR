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


letra('when only of in this Spaces present one but returns included that in passed presents')
