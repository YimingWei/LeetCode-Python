class UnionFind:
    def __init__(self) -> None:
        """
        记录每个节点的父节点
        记录每个节点到父节点的权重
        """
        self.father = {}
        self.value = {}

    def add(self, x):
        """
        添加新节点
        初始化权重为1
        """
        if x not in self.father:
            self.father[x] = None
            self.value[x] = 1.0

    def find(self, x):
        """
        查找根节点
        路径压缩
        更新权重
        """
        root = x
        # 节点更新权重要放大的倍数
        base = 1

        while self.father[root] != None:
            root = self.father[root]
            base *= self.value[root]
        # 路径压缩，提升查找效率
        while x != root:
            orignal_father = self.father[x]
            # 离根节点越远放大倍数越高
            self.value[x] *= base
            base /= self.value[orignal_father]
            self.father[x] = root
            x = orignal_father
        return root

    def merge(self, x, y, val):
        """
        合并两个节点
        """
        root_x, root_y = self.find(x), self.find(y)

        if root_x != root_y:
            self.father[root_x] = root_y
            self.value[root_x] = self.value[y] * val / self.value[x]

    def is_connected(self, x, y):
        """
        判断两个节点是否相连
        """
        return x in self.value and y in self.value and self.find(x) == self.find(y)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (a, b), val in zip(equations, values):
            uf.add(a)
            uf.add(b)
            uf.merge(a, b, val)

        res = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if uf.is_connected(a, b):
                res[i] = uf.value[a] / uf.value[b]
        return res
