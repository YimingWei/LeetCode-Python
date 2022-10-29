class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_cnt = list(collections.Counter(tasks).values())
        max_cnt = max(task_cnt)
        num_max_cnt = task_cnt.count(max_cnt)
        return max((max_cnt-1) * (n + 1) + num_max_cnt, len(tasks))
