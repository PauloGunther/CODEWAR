def vogais(texto):
    c = 0
    for i in str(texto):
        if i in 'aeiou':
            c += 1
    print(c)


vogais('Carro usado nao abre')
