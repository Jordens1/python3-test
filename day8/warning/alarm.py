
def compare(obj):

    a = obj['mem_total']
    c = obj['mem_free']
    if (c / a)* 100 < 80:
        return 1

    else :
        return 0


