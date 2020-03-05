def solve(str1):
    data = []
    if str1[0].isdigit():
        data.append(0)
    for i in range(1, len(str1)):
        if str1[i].isdigit() ^ str1[i-1].isdigit():
            data.append(i)
    if str1[-1].isdigit():
        data.append(len(str1))
    strmax = ""
    for i in range(len(data)):
        if i < len(data) / 2:
            start = data[i*2]
            end = data[i*2 + 1]
            if start != 0:
                if str1[start-1] == "+" or line[start - 1] == "-":
                    start -= 1
            if end < len(str1) and str1[end] == "." and (i+1) * 2 < len(data) and data[(i+1)*2] == end + 1:
                end = data[(i+1)*2 + 1]
            if len(strmax) <= end - start:
                strmax = str1[start: end]
    print(data)
    return "".join(strmax)


if __name__ == '__main__':
    while True:
        line = str(input()).strip()
        print(solve(line))