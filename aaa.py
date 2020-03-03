# coding:utf-8

import re

while True:
    line = str(input())
    pat = re.compile(r"\d+")
    s = pat.finditer(line)
    tmp = []
    for i in s:
        tmp.append((i.group(), i.regs[0]))
    max_int = max(map(int, [c[0] for c in tmp]))
    tmp = [i for i in tmp if i[0] == str(max_int)]
    print(tmp)
    find = []
    for t in tmp:
        inx = t[1][1]
        xiaoshu = ""
        f = t[0]
        if len(line) != inx and line[inx] == ".":
            _inx = inx
            for c in range(len(line)[inx+1:]):
                if line[_inx+1].isdigit():
                    _inx+=1
                else:
                    break
            xiaoshu = line[inx+1: _inx+1]

        if xiaoshu:
            f = t[0] + "."+xiaoshu
        find.append(f)

    find = max(map(float, find))
    print(find)
