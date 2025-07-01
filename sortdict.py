dict = {
    'Ram':2,
    'Sham':5,
    'Ban':4
}
print(f'Original dict: {dict}')
listdic = list(dict.keys())
listdic.sort()
sortdicbykey = {i: dict[i] for i in listdic}
print(f'Sort by keys: {sortdicbykey}')
sortdicbyval = {k: v for k,v in sorted(dict.items(), key=lambda item: item[1])}
print(f'Sort by value: {sortdicbyval}')

