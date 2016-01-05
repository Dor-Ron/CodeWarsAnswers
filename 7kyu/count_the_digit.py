def nb_dig(n, d):
    return "".join(filter(lambda x: str(d) in x, [str(pow(num, 2)) for num in xrange(n+1)])).count(str(d))
