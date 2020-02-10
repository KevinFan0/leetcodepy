# coding:utf-8
# KMP算法

def kmp(mom_string, son_string):
    # 传入一个母串和一个子串
    # 返回子串匹配上的第一个位置，若没有匹配上则返回-1
    # 母指针和子指针初始化为0
    if len(son_string) == 0:
        return 0
    if len(mom_string) == 0:
        return 0
    # 求next数组
    nextlist = [-1] * len(son_string)
    if len(son_string) > 1:
        # 这里加if是怕列表越界
        nextlist[1] = 0
        i, j = 1, 0
        while i < len(son_string) - 1:
            # 这里一定要-1，不然会出现越界
            if j == -1 or son_string[i] == son_string[j]:
                i += 1
                j += 1
                nextlist[i] = j
            else:
                j = nextlist[j]
    m = s = 0
    while s < len(son_string) and m < len(mom_string):
        # 匹配成功，或者遍历完母串匹配失败退出
        if s == -1 or mom_string[m] == son_string[s]:
            m += 1
            s += 1
        else:
            s = nextlist[s]

    if s == len(son_string):
        # 匹配成功
        return m - s
    # 匹配失败
    return -1

if __name__ == '__main__':
    mom_string = 'ababababca'
    son_string = 'abababca'
    print(kmp(mom_string, son_string))