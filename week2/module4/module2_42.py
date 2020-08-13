import os

lst = []
for d, _, f in os.walk('../../../main'):
    for i in f:
        if '.py' in i:
            if lst is None or d not in lst:
                lst.append(d)

print(lst)

with open('res.txt', 'w') as f:
    f.writelines('\n'.join(lst))
