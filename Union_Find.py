# Union-Find算法实现

class UF:
    def __init__(self, n):
        self.count = n
        self.parent = [0 for _ in range(n)]
        self.size = [0 for _ in range(n)]       # size记录树的权重
        for i in range(n):
            self.parent[i] = i
            self.size[i] = 1

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP == rootQ:
            return

        # 小树接到大树下面，较平衡
        if self.size[rootP] > self.size[rootQ]:
            self.parent[rootQ] = self.parent[rootP]
            self.size[rootP] += self.size[rootQ]
        else:
            self.parent[rootP] = self.parent[rootQ]
            self.size[rootQ] += self.size[rootP]
        self.count -= 1


    def connected(self, p, q):
        # 判断p和q是否互相连通
        rootP = self.find(p)
        rootQ = self.find(q)
        return rootP == rootQ


    def find(self, x):
        # 返回某个节点x的根节点
        while self.parent[x] != x:
            # 进行路径压缩
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def count(self):
        return self.count