def tempo(k):
    h = k // 3600
    m = (k % 3600) // 60
    print(f'{h}:{m}')

tempo(46984)
