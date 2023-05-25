class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def recur(curr_n, curr_arr):
            if curr_n == 0:
                return curr_arr

            # print(curr_n, curr_arr, len(curr_arr))

            curr_n = curr_n - 1
            gen_arr = set()

            for elem in curr_arr:
                if len(elem) == 0:
                    gen_arr.add("()")
                for i in range(len(elem)):
                    if i == 0 or elem[i] == ")":
                        new_str = elem[:i] + "()" + elem[i:]
                        gen_arr.add(new_str)
            # if curr_arr == []:
            #     gen_arr = ["()"]
            #     print(curr_n + 1)
            # else:
            #     for elem in curr_arr:
            #         for i in range(len(elem)):
            #             if i == 0 or elem[i] == ")":
            #                 new_str = elem[:i] + "()" + elem[i:]
            #                 gen_arr.add(new_str)
            return recur(curr_n, list(gen_arr))
        return recur(n, [""])