# coding:utf-8
import json

"""
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
"""

class Solution:
    def canCompleteCircuit2(self, gas, cost) -> int:
        # 该方法时间复杂度为n2
        # 先判空
        ret = -1
        if len(gas) == 0 or len(cost) == 0:
            return ret
        # 一个for循环找到合适的出发车站
        for i in range(len(gas)):
            g, c = gas[i], cost[i]
            r = g - c  # 剩余的油
            if r < 0:
                continue
            else:
                # 拼成两个新的gas和cost
                gasnew = gas[i:] + gas[:i]
                costnew = cost[i:] + cost[:i]
                if self.carrunnext(gasnew, costnew):
                    ret = i
                    break
                else:
                    continue
        return ret

    def carrunnext(self, gas, cost):
        print(gas, cost)
        r = gas[0]
        for i in range(len(gas) - 1):
            # 开往n+1站
            r = r - cost[i] + gas[i + 1]
            if r < cost[i + 1]:
                return False
        return True


    def canCompleteCircuit(self, gas, cost) -> int:
        n = len(gas)

        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(n):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0

        return starting_station if total_tank >= 0 else -1

    def canCompleteCircuit3(self, gas, cost) -> int:
        # 先判空
        ret = -1
        current, total = 0, 0
        if len(gas) == 0 or len(cost) == 0:
            return ret
        # 一个for循环找到合适的出发车站
        for i in range(len(gas)):
            current += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if current < 0:
                stationindex = i + 1
                current = 0
        if total >= 0:
            ret = stationindex
        return ret

def stringToIntegerList(input):
    return json.loads(input)


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            gas = stringToIntegerList(line)
            line = next(lines)
            cost = stringToIntegerList(line)

            ret = Solution().canCompleteCircuit(gas, cost)

            out = str(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()