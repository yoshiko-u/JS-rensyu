animals = [{'猫','三毛'},{'犬','コーギー'},{'猫','シャム'},{'犬','ダックス'},{'犬','黒ラブ'}]

d = {}
for k, v in animals:
    if k not in d:
        d[k] = [v]
    else:
        d[k].append(v)
print(d)