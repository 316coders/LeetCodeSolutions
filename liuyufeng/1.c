/**
 * 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

解题思路：（1）两个for循环
（2）先排序，用二分法查找
（3）用harsh列表，用target值减去扫描初始值，然后与链表内值做比较。
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int *res = (int *) malloc (sizeof(int) * 2); 
    * returnSize = 2;

    for(int i = 0; i < numsSize; i ++)
    {
        for(int j = i+1; j < numsSize; j++)
        {
            if(nums[i] + nums[j] == target)
            {
                res[0] = i;
                res[1] = j;
            }
        }
    }
    return res;
}