# 四则运算表达式利用栈来实现
# 将中缀表达式转为后缀表达式
# “中缀表达式“9+(3-1)×3+10÷2”转化为后缀表达式“9 3 1-3*+10 2/+”


def stackexpression(expression):
    stack, res, num = [], [], 0
    sign_maps = {
        "+": 0,
        "-": 0,
        "*": 1,
        "/": 1
    }
    pro_sign = ["*", "/"]
    for item in expression:
        if item.isnumeric():
            # num = num * 10 + int(item)
            res.append(item)
        else:
            if item == ")":
                # 找到前面的"("并把两者直接的符号输出
                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == "(":
                        stack.pop(i)
                        break
                    else:
                        res.append(stack.pop())
            elif item in pro_sign:
                for i in range(len(stack)-1, -1, -1):
                    if sign_maps[item] > sign_maps[stack[i]]:
                        stack.append(item)
                        break
                    else:
                        res.append(stack.pop())
                else:
                    stack.append(item)
            else:
                stack.append(item)

    while stack:
        res.append(stack.pop())
    res = "".join(res)

    return res


expression = "3+(6*7-20)+2*3"

# def middle2behind(expresssion):
#     result = []             # 结果列表
#     stack = []              # 栈
#     for item in expresssion:
#         if item.isnumeric():
#             result.append(item)
#         else:
#             if len(stack) == 0:
#                 # 如果栈为空则直接入栈
#                 stack.append(item)
#             elif item in "*/(":
#                 # 如果当前字符为高优先级则入栈
#                 stack.append(item)
#             elif item == ")":
#                 # 如果为右括号则全部弹出（碰到左括号停止）
#                 t = stack.pop()
#                 while t != "(":
#                     result.append(t)
#                     t = stack.pop()




if __name__ == '__main__':
    exp = "9+(3-1)*30+9/2"
    print(stackexpression(exp))