def soma(num):
    while len(str(num)) > 1:
        a = 0
        for i in str(num):
            a += int(i)
        num = a
    print(a)


soma(9429999)