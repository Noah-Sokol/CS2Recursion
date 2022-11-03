def get_square_root(n,p,e):
    n = float(n)
    p = float(p)
    e = float(e)
    if1 = (e*2)-2
    if abs(if1) < p:
        return e
    else:
        return get_square_root(n,p,(((e+n)/e)/2))