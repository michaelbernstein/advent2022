lines = open('input.txt', 'r').readlines()

def expand(r):
    numbers = r.split('-')
    return (int(numbers[0]), int(numbers[1]))

def inside_range(one, two, check_overlap=False):
    if one[0] <= two[0] and one[1] >= two[1]:
        return True
    elif two[0] <= one[0] and two[1] >= one[1]:
        return True
    
    if check_overlap:
        x = list(set(range(one[0], one[1] + 1)) & set(range(two[0], two[1] + 1)))
        if len(x) > 0:
            return True 
    return False

count = 0
overlap_count = 0 
for l in lines:
    r = l.strip().split(',')
    one = expand(r[0])
    two = expand(r[1])
    if inside_range(one, two, False):
        count += 1
    if inside_range(one, two, True):
        overlap_count += 1
print("Full overlap:", count)
print("Total overlaps:", overlap_count)

