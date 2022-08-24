class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board) #行数
        n = len(board[0]) #列数
        visited = [[False for _ in range(n)] for _ in range(m)] #记录网格的访问状态
        # (row[i], col[i])表示行列的偏移量，比如(-1, 0)表示向上移一格
        row = [-1, 0, 1, 0]
        col = [0, 1, 0, -1]

        def dfs(x, y, idx):
            """
            x: 行索引
            y: 列索引
            idx: word字母索引
            """
            if board[x][y] != word[idx]: #当前board的字母与word的idx处字母不同，则此路不通，返回False，赶紧向其他方向搜索
                return False
            if idx == len(word)-1: #此时已经遍历到word的最后一个字母，说明路找对了
                return True
            visited[x][y] = True #标记
            for i in range(4): #向当前位置的"上、右、下、左"4个方向搜索word里的字母
                nx = x + row[i]
                ny = y + col[i]
                if 0<=nx<m and 0<=ny<n and visited[nx][ny]==False and dfs(nx, ny, idx+1):
                    return True
            visited[x][y] = False #能走到这一步，说明这条路不对，把标记过已访问的状态解除
            return False
        
        for x in range(m):
            for y in range(n):
                if dfs(x, y, 0):
                    return True
        return False
