class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])
        
        if not (cnt := Counter(word)) <= Counter(chain(*board)):
            return False     
        
        def recur(curr_str, curr_set, curr_i, curr_j):
            if curr_str == word:
                return True
            if len(curr_str) > len(word):
                return False
            elif curr_str != word[:len(curr_str)]:
                return False
            
            for direction in directions:
                new_i = curr_i + direction[0]
                new_j = curr_j + direction[1]
                if not(0 <= new_i < m and 0 <= new_j < n):
                    continue
                
                if board[new_i][new_j] != word[len(curr_str)]:
                    continue
                
                string = str(new_i) + "-" + str(new_j)
                if string in curr_set:
                    continue
                curr_set.add(string)
                return_value = recur(curr_str + board[new_i][new_j], curr_set, new_i, new_j)
                curr_set.remove(string)
                if return_value == True:
                    return True
            return False
        
        # check for first letter
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    string = str(i) + "-" + str(j)
                    if recur(board[i][j], { string }, i, j) == True:
                        return True
        return False