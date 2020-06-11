
// 请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

// 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

// 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

int *dailyTemperatures(int *T, int TSize, int *returnSize)
{
    int *monoStack = (int *)malloc(sizeof(int) * TSize);
    memset(monoStack, 0, sizeof(int) * TSize);
    int stackTop = -1;
    int tIter = 0;

    int *res = (int *)malloc(sizeof(int) * TSize);
    memset(res, 0, sizeof(int) * TSize);

    while (tIter < TSize) {
        /* monoStack[stackTop]是栈顶元素在T中的下标，T[monoStack[stackTop]] 才是真正的栈顶温度 */
        while (stackTop != -1 && T[monoStack[stackTop]] < T[tIter]) {
            int r = monoStack[stackTop];
            stackTop--;
            
            res[r] = tIter - r;
        }
        monoStack[++stackTop] = tIter++;        
    }
    *returnSize = TSize;
    return res;
}