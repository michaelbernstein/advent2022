def is_start_marker(str, idx, length):
    if len(set(str[idx-length:idx])) == length:
        return True
    return False
     
def find_start_marker(str, length):
    for idx, s in enumerate(str):
        if idx < length:
            continue
        if is_start_marker(str, idx, length):
            return idx
    return -1

str = open('input.txt', 'r').readlines()[0]
print(find_start_marker(str, 4))
print(find_start_marker(str, 14))
