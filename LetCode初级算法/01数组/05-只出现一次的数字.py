"""
如何才能做到线性时间复杂度和常数空间复杂度呢？

答案是使用位运算。对于这道题，可使用异或运算 \oplus⊕。异或运算有以下三个性质。

任何数和 00 做异或运算，结果仍然是原来的数，即 a \oplus 0=aa⊕0=a。
任何数和其自身做异或运算，结果是 00，即 a \oplus a=0a⊕a=0。
异或运算满足交换律和结合律，即 a \oplus b \oplus a=b \oplus a \oplus a=b \oplus (a \oplus a)=b \oplus0=ba⊕b⊕a=b⊕a⊕a=b⊕(a⊕a)=b⊕0=b。

使用异或运算，将所有值进行异或
异或运算，相异为真，相同为假，所以 a^a = 0 ;0^a = a
因为异或运算 满足交换律 a^b^a = a^a^b = b 所以数组经过异或运算，单独的值就剩下了

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[0] ^= nums[i]
        return nums[0]