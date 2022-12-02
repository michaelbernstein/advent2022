lines = open('input1.txt', 'r').readlines()
  
list = []
count = 0

for l in lines:
    if l == "\n":
        list.append(count)
        count = 0
    else:
        count += int(l)
list.sort(reverse=True)
print(sum(list[0:3]))
