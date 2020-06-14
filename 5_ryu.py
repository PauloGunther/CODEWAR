# MAIOR DISTANCIA ENTRE DETERMINADOS PONTOS
def best(t, k, xs):
    """
    t: maior distancia aceita
    k: numero de pontos
    xs: lista de pontos
    """
    from itertools import combinations
    M = []
    for i in combinations(xs, k):
        if sum(i) <= t:
            M.append(sum(i))
    try:
        r = max(M)
    except:
        return None
    else: 
        return r

