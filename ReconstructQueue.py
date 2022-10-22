class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按照p[0]降序、p[1]升序排列数对
        people = sorted(people, key=lambda p: (-p[0], p[1]))
        res = []
        # 再根据p[1]重排序
        for p in people:
            if len(res) <= p[1]:
                res.append(p)
            else:
                res.insert(p[1], p)
        return res
