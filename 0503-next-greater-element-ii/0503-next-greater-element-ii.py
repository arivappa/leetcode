class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        mon_stack = deque()
        return_arr = [-1]*len(nums)
        for i in range(len(nums)-1, -1, -1):
            curr_num = nums[i]
            if len(mon_stack) > 0:
                top_most_elem = mon_stack[-1]
            else:
                top_most_elem = -inf
            if top_most_elem > curr_num:
                return_arr[i] = top_most_elem
                mon_stack.append(curr_num)
                continue
            while len(mon_stack) > 0 and mon_stack[-1] <= curr_num:
                mon_stack.pop()
            if len(mon_stack) > 0:
                return_arr[i] = mon_stack[-1]
            mon_stack.append(curr_num)
        # print(mon_stack)
        # print(return_arr)
        
        for i in range(len(nums)-1, -1, -1):
            if return_arr[i] == -1 or True:
                curr_num = nums[i]
                if len(mon_stack) > 0:
                    top_most_elem = mon_stack[-1]
                else:
                    top_most_elem = -inf
                if top_most_elem > curr_num:
                    return_arr[i] = top_most_elem
                    mon_stack.append(curr_num)
                    continue
                while len(mon_stack) > 0 and mon_stack[-1] <= curr_num:
                    mon_stack.pop()
                if len(mon_stack) > 0:
                    return_arr[i] = mon_stack[-1]
                mon_stack.append(curr_num)

        # print(mon_stack)
        # print(return_arr)
        
        return return_arr

    
## no documentation :(