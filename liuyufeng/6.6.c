
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。



int cmp(const void *a, const void *b) {
    return (long) * (int * ) a - (long) * (int *) b;
}
int longestConsecutive(int *nums, int numsSize) { 
    if (numsSize == 0 ) return 0;
    qsort(nums, numsSize, sizeof(int), cmp);            //快速排序
    int *dp = malloc(sizeof(int) * numsSize);            // dp[i]: 表示以i为结尾连续序列长度
        dp[0] = 1;
        int max = 1;
        for (int i = 1; i < numsSize; i++) {
            if(nums[i] == nums[i - 1] + 1) 
                dp[i] = dp[i-1]+1;
                else if(nums[i] == nums[i-1])
                    dp[i] = dp[i-1];
                    else 
                    dp[i] = 1;
                    max = fmax(max, dp[i]);
        }
        return max;
    
}