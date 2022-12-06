def init_stacks(ls, s):
    c = 0
    for l in ls:
        p = list(l.strip())
        c += 1
        if p[0] == "1":
            for i in range(0, int(p[-1])):
                stacks.append([])
            return c

def load_board(s,lines):
    for l in lines:
        for i in range(1,len(l),4):
            if l[i] != ' ':
                s[i//4].insert(0,l[i])

def move(s, count, start, end):
    for i in range(0,count):
        s[end].append(s[start].pop())

def move_9001(s, count, start, end):
    temp = []
    for i in range(0, count):
        temp.append(s[start].pop())
    for i in range(0, count):
        s[end].append(temp.pop())

def print_stacks(s):
    str = ""
    for st in s:
        if st != []:
            str = str + st[-1]
        else:
            str = str + " "
    print(str)


lines = open('input.txt', 'r').readlines()
stacks = []
c = init_stacks(lines, stacks)
load_board(stacks, lines[0:c-1])

for l in lines[c:len(lines)]:
    tokens = l.strip().split()
    if tokens != []:
        move(stacks, int(tokens[1]),int(tokens[3])-1,int(tokens[5])-1)
print_stacks(stacks)

stacks = []
c = init_stacks(lines, stacks)
load_board(stacks, lines[0:c-1])
for l in lines[c:len(lines)]:
    tokens = l.strip().split()
    if tokens != []:
        move_9001(stacks, int(tokens[1]),int(tokens[3])-1,int(tokens[5])-1) 
print_stacks(stacks)
