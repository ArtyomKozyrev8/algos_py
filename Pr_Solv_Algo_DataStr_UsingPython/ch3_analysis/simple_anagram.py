def check_simple_anagram(s1: str, s2: str) -> bool:
    """
    We consider only simplest words, we do not consider that
    s1 or s2 can contain ' ',  '!', '.' or other punctuation symbols
    """
    if len(s1) != len(s2):
        return False

    symbols_dict = dict()
    for i in s1:
        if i not in symbols_dict:
            symbols_dict[i] = 1
        else:
            symbols_dict[i] += 1

    for i in s2:
        if i not in symbols_dict:
            return False
        else:
            symbols_dict[i] -= 1
            if symbols_dict[i] < 0:
                return False

    return True
