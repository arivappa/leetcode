class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return_arr = []
        def recur(curr_index, curr_arr, curr_len):
            if curr_len == k:
                return_arr.append(curr_arr)
                return
            if curr_index > n:
                return
            recur(curr_index + 1, curr_arr, curr_len)
            recur(curr_index + 1, curr_arr + [curr_index], curr_len + 1)
        recur(1, [], 0)
        return return_arr