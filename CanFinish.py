class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 创建图
        ## 创建节点
        nodes = dict()
        for i in range(numCourses):
            nodes[i] = []
        ## 创建边
        for e in prerequisites:
            nodes[e[1]].append(e[0])
        
        # 拓扑排序(Topological Sort)
        indegrees = dict()
        ## 初始化入度
        for i in range(numCourses):
            indegrees[i] = 0
        ## 根据边的方向给每个节点的入度赋值
        for e in prerequisites:
            indegrees[e[0]] += 1
        # 有向无环图
        ## 初始化队列
        q = deque()
        ## 把入度为0的节点加入队列
        for key in indegrees.keys():
            if indegrees[key] == 0:
                q.append(key)
        cnt = 0
        ## 节点消除后,该节点指向的所有子节点的入度减一,然后把入度为0的节点再加入q
        while q:
            cur = q.popleft()
            cnt += 1
            for children in nodes[cur]:
                indegrees[children] -= 1
                if indegrees[children] == 0:
                    q.append(children)
        if cnt == numCourses:
            return True
        return False
