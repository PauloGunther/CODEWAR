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


accum('bares')
