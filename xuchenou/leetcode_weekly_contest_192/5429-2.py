class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        # 先排序求中位数
        arr = sorted(arr)
        mid = arr[(n - 1) // 2]

        def mykey(x):
            # 自定义最强排序的key函数
            # 注意py 3不同于其他语言的传入两个参数的自定义比较函数
            # 此处的意思代表先按照abs升序排列, 相等情况下再按照自身的值的升序排列
            return (abs(x - mid), x)

        # 按照最强排序后取最后的k个即为所求
        arr = sorted(arr, key=mykey)
        return arr[n - k:]

作者：suibianfahui
链接：https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array/solution/di-192-chang-zhou-sai-ti-jie-by-suibianfahui-3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。