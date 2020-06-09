
// 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

// 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

// 注意：给定 n 是一个正整数。

// 示例 1：

// 输入： 2
// 输出： 2
// 解释： 有两种方法可以爬到楼顶。
// 1.  1 阶 + 1 阶
// 2.  2 阶
// 示例 2：

// 输入： 3
// 输出： 3
// 解释： 有三种方法可以爬到楼顶。
// 1.  1 阶 + 1 阶 + 1 阶
// 2.  1 阶 + 2 阶
// 3.  2 阶 + 1 阶


// 解题思路：这里做了一个临时的keymap，对于已计算过的直接取值。
// 初始化时，注意要申请n+1个数的空间，因为n从1开始，有n个数。0可以不用，因为根据退出条件不会走到0。
// 退出条件n=1和n=2对应的值，也要在初始化时赋值到keymap里。

int _clibStairs(int n, int *keyMap)
{
   if (keyMap[n]) {
        return keyMap[n];
    }
    int ret = keyMap[n] = _clibStairs(n-1, keyMap) + _clibStairs(n-2, keyMap);
    return ret;

}

int climbStairs(int n){
    if (n < 0)
        return 0;
    if (n <= 2)
        return n;
        
    int *keyMap = calloc((n+1) ,sizeof(int));
    keyMap[1] = 1;
    keyMap[2] = 2;
    return _clibStairs(n , keyMap);

}
