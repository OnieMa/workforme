class Solution:
    def get_num(self, n: int):
        num = str(n)
        sum = 0
        for i in num:
            m = int(i)
            sum += m ** 2
        print("sum =", sum)
        return sum

    # maaoyu 使用集合实现
    def isHappy(self, n: int) -> bool:
        res = self.get_num(n)
        li = set()
        while 1:
            if res == 1:
                return True
            elif res in li:
                return False
            else:
                res = self.get_num(res)
                li.add(res)
                print("li :", li)


    # 集合实现
    def isHappy1(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            new_num = 0
            n_str = str(n)
            for i in n_str:
                new_num += int(i) ** 2
            if new_num == 1:
                return True
            else:
                n = new_num
        return False

if __name__ == '__main__':
    print(Solution().isHappy(20))
