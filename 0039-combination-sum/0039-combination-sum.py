class Solution(object):
    def combinationSum(self, candidates, target):
        res = []

        def backtrack(start, path, current_sum):
            if current_sum == target:
                res.append(list(path))
                return

            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, current_sum + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
        
        