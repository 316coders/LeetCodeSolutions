
给你一个数组 nums ，数组中有 2n 个元素，按 [x1,x2,...,xn,y1,y2,...,yn] 的格式排列。

请你将数组按 [x1,y1,x2,y2,...,xn,yn] 格式重新排列，返回重排后的数组。

 

示例 1：

输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]
示例 2：

输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]
示例 3：

输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]

思路：先排序n之前的偶数位，再排序n之后的奇数位，

int* shuffle(int* nums, int numsSize, int n, int* returnSize){
    int *res;
    for(int i = 0; i < numsSize; i++) {
        if(i<n) {
            res[2*i] = nums[i]; 
        }else if(n <= i) {
            for(int j = 1; j <= n; j++) {
                res[2*j-1] =  nums[i];
            }
        }
       
    }
    return *res;
}


int* shuffle(int* nums, int numsSize, int n, int* returnSize){
   int length = numsSize;
    char *res = (char*)malloc(sizeof(char)*length);
    for(int i = 0; i < numsSize; i++) {
        if(i<n) {
            res[2*i] = nums[i]; 
        }else if(n <= i) {
            for(int j = 1; j <= n; j++) {
                res[2*j-1] =  nums[i];
            }
        }
       
    }
    return res;
}


解题思路
（1）先申请2n大小数组res的内存空间；
（2）然后对这个数组进行初始化处理；
（3）然后分别把原数组nums内的元素，分成两部分处理，前n个数，放到res的2i的位置（即偶数的位置），后n个数，放到res的2j-1的位置（即奇数的位置）。
最后返回数组res就行啦

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* shuffle(int* nums, int numsSize, int n, int* returnSize){
   int length = 2*n;
    int *res = (int*)malloc(sizeof(int)*length);        //申请内存；
    if(res == NULL) {
        return NULL;
    }
    memset(res, 0, sizeof(int) * length);           //初始化处理设置res的初始值为0；
    int j = 1;
    for(int i = 0; i < numsSize; i++) {
        if(i<n) {
            res[2*i] = nums[i]; 
        }else {
            res[2*j-1] =  nums[i];
            j++;
        }
       
    }
    *returnSize = length;
    return res;
}

