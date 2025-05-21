def count(s):
    dicti = {}
    ggs = [c for c in s.lower() if c not in " ., "]
    for c in ggs:
        if c in dicti:
            dicti[c] += 1
        else:
            dicti[c] = 1
    return dicti

def combine(dict1, dict2):
    dici = {}
    for keys, value in dict2:
        dici[keys] = value
    for keys, value in dict1:
        dici[keys] = value
    return dici

