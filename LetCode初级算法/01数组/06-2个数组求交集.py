class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        '''
        思路1：暴力查找法
        '''
        # res = []
        # for k in nums1:
        #     index=-1
        #     for j in range(0, len(nums2)):
        #         if nums2[j]==k:#当第1个列表的元素，在第2个列表中出现时，则将该元素添                                 #加到结果集中
        #             index = j
        #             break
        #     if index!=-1:
        #         res.append(k)
        #         del nums2[index]#在第2个列表中删除这个元素
        # return res
        '''
        思路2：
        '''
        # res = []
        # map = {}
        # for i in nums1:
        #     #用字典统计第1个列表中出现了哪些数，以及出现的次数
        #     map[i] = map[i] + 1 if i in map else 1
        # for j in nums2:
        #     #遍历第2个列表，发现同时出现在map中的，且这个出现次数>0的，加入到结果res
        #     if j in map and map[j]>0:
        #         res.append(j)
        #         #每加入1个元素，就对map进行更新
        #         map[j] -= 1
        # return res
        '''
        思路3：可以提高效率
        1.先对第2个列表排序
        2.再每次检查元素是否出现时，用二分搜索
        '''
        res = []
        nums2.sort()
        for k in nums1:
            flag, j = self.binarySearch(nums2, k)
            if flag:
                res.append(k)
                del nums2[j]
        return res

    def binarySearch(self, nums, num):
        # 二分查找，比较一半的列表，循环左右侧比较
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = int((left+right)/2) # 取中间索引
            print("mind", left, right, mid)
            if nums[mid] == num:
                return True, mid
            if nums[mid]<num:#这个数<要查找的数，left指针向mid+1移动
                left = mid+1
            else:
                right = mid-1
        return False, 0#这里是没有找到要查找的元素

    def intersect2(self, nums1, nums2):
        # 生成nums1的 元素次数
        res = []
        map = {}
        for i in nums1:
            map[i] = map[i] + 1 if i in map else 1
        # 对比nums2,将相同的数，增加到res中，并map计数减1s
        for j in nums2:
            if j in map and map[j] >0:  # 2个条件判断
                res.append(j)
                map[j] -= 1
        return res


def binarySearch(nums, num):
    left = 0
    rigtht = len(nums) -1
    while left <=rigtht:
        mid = int((left + rigtht)/2)
        print("mid", left, rigtht, mid)
        if nums[mid] == num:
            return True, mid
        if nums[mid] < num:
            left = mid + 1
        else:
            rigtht = mid -1
    return False, 0


if __name__ == '__main__':
    nums = [2, 3, 4, 10, 40]
    num = 10
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    #print(binarySearch(nums, num))
    s= Solution()
    print(s.intersect2(nums1, nums2))