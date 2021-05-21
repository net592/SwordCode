import random
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        # 解法1 暴力穷举，空间复杂度2n 
        # aux = copy.deepcopy(self.array)

        # for idx in range(len(self.array)):
        #     remove_idx = random.randrange(len(aux))
        #     print(idx, aux)
        #     self.array[idx] = aux.pop(remove_idx)

        # 解法2 空间置换
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array