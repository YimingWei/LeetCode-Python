class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        self.head = ListNode()
        self.tail = ListNode()
        # 初始化head <-> tail
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_node_to_tail(self, key):
        # 先将哈希表key指向的节点取出来
        node = self.hashmap[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 再插入到尾节点前
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node #尾节点前一个节点的后向指针，指向node
        self.tail.prev = node #尾节点的前向指针，指向node

    def get(self, key: int) -> int:
        if key in self.hashmap:
            # 如果key已经在hashmap中则把它已到末尾
            self.move_node_to_tail(key)
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            # 如果key已经在hashmap里面则需要改变对应的值
            self.hashmap[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.hashmap) == self.capacity: #如果已经达到容量极限
                self.hashmap.pop(self.head.next.key) #在hashmap里剔除头节点后的那个节点
                self.head.next = self.head.next.next #在链表中剔除节点
                self.head.next.prev = self.head
            # key不在hashmap里面，则插入到尾节点前
            new = ListNode(key, value)
            self.hashmap[key] = new
            new.prev = self.tail.prev #c一定要在d之前
            new.next = self.tail #b
            self.tail.prev.next = new #a一定要在d之前
            self.tail.prev = new #d
            
