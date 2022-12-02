def swap(dict, set1):
    for key, values in list(dict.items()):
        if key in set1:
            dict[values] = key
            del dict[key]

