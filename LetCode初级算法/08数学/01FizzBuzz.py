class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # 初始一个数组
        res = []
        
        for num in range(1, n+1):
            # 判断数整除情况
            div3 = (num % 3 == 0)
            div5 = (num % 5 == 0)

            num_str = ""
            if div3:
                num_str += "Fizz"
            if div5:
                num_str += "Buzz"
            print(div3, div5)
            if not div3 and not div5:
                print(div3, div5)
                num_str = str(num)
            res.append(num_str) 
        return res