import functools as f

lines = open('input.txt', 'r').readlines()
values = []
for l in lines:
    p = list(l.strip())


    duplicates = []
    p = list(l.strip())
    c = len(p)
    if c % 2 == 0:
        c2 = len(p)//2
        for x in range (c2):
            for y in range(c2, c):
                if p[x] == p[y] and p[x] not in duplicates:
                    values.append(p[x])
                    duplicates.append(p[x])
    else:
        c2 = len(p)//2 - 1
        for x in range(c2):
            for y in range(c2,c):
                if p[x] == p[y] and p[x] not in duplicates:
                    duplicates.append(p[x])
                    values.append(p[x])
 
    sum = 0
    for i in values:
        z = ord(i)
        if z >= 97:
            sum += z - 96
        elif z >=65 and z <= 90: 
            sum += z - 38
print(sum)


def triplicated(list):
    for e in list[0]: 
        if e in list[0] and e in list[1] and e in list[2]:
            return e
    return ""

lines = open('input.txt', 'r').readlines()
combined = []
counter = 0
results = []
for l in lines:
    combined.append(l.strip())
    counter += 1
    if counter == 3:
        r = triplicated(combined)
        if r != "":
            results.append(r)
        combined = []
        counter = 0 

sum = 0
for i in results:
    z = ord(i)
    if z >= 97:
        sum += z - 96
    elif z >=65 and z <= 90: 
        sum += z - 65 + 27
print(sum)