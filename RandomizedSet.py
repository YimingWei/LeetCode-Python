class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.idx_map = dict()


    def insert(self, val: int) -> bool:
        if val not in self.idx_map:
            self.idx_map[val] = len(self.nums)
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # 将要删除的val与nums最后一个数交换，然后nums删除最后一个数，耗时为O(1)
        if val in self.idx_map:
            swap_val, idx = self.nums[-1], self.idx_map[val]
            self.nums[idx] = swap_val
            self.idx_map[swap_val] = idx
            self.nums.pop()
            del self.idx_map[val]
            return True
        return False


    def getRandom(self) -> int:
        return choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
