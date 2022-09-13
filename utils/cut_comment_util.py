def get_cut(cut, poly, sym):
    if cut == 'EX' and poly == 'EX' and sym == 'EX':
        return '3EX'
    elif cut == 'EX' and (poly != 'EX' or sym != 'EX'):
        return 'EX'
    else:
        return cut
