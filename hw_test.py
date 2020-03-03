def solve(line):
    str1 = list(line)
    data = []
    if str1[0].isdigit() or str1[0] in ["+", "-"]:
        data.append(0)
    for i in range(1, len(str1)):
        if (str1[i].isdigit() and (str1[i-1].isdigit() or str1[i-1] == ".")) or (str1[i-1].isdigit() and str1[i] == "." and str1[i+1].isdigit()):
            data.append(i)
    if str1[-1].isdigit():
        data.append(len(str1))
    cur, ptr = 0, 1
    while ptr < len(data):
        if data[ptr] - ptr == data[cur] - cur:
            ptr += 1
        else:
            cur += 1
            ptr += 1
    print("".join(str1[data[cur]-1: data[ptr-1]]))



if __name__ == '__main__':
    while True:
        line = str(input())
        solve(line)