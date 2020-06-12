def numero(num):
    s = 0
    for i in range(0, num):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print(s)


numero(15)
