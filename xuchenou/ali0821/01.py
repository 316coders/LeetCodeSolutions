import sys
from typing import List
#一次两个人，过河时间为体重较大的人的体重，所以大体重绑在一起
#如果有一个人就是一个人的时间，最轻的一个人过
#计算过河时间
#注意来回时间，所以要有一个最轻的负责开船回来
"""
2 10 11 12
时间=  12 + 2 + 11 + 2 + 10（2） =37
4个人需要 3个最重+ 2个最轻时间
最后一趟不用回来
n个人 n-1个最重 + n-2次最轻

3个人需要 2两个最重 + 1个最轻
2个人需要 1个最重
1个人需要 1个最重

2 3 7 8
时间 = 8 + 2 + 7 + 2 + 3（2） = 22 ？

"""

#T组测试数据
"""
T 组数
n  人数
a[0]  a[1]  a[2]
n  人数
b[0]  b[1]  b[2] ......
"""

if __name__ == "__main__":
    # 读取一共的数据组数
    T = int(sys.stdin.readline())
    for i in range(T):
        # 读第一行是每组的人数
        num_people = sys.stdin.readline()
        line_pounds = sys.stdin.readline()
        # 第二行读入一个list
        pounds = sorted(list(map(int, line_pounds.split())))
        #print(pounds)
        if (num_people) <= 2:
            time = pounds[-1]
        else:
            time = pounds[0] * (int(num_people) - 2) + sum(pounds[1:])
        print(time)
