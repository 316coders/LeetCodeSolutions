最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 

示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

解题思路：只进行一次遍历，然后采用双指针，前指针和后指针，通过移动指针来判断三个数的和与目标值的关系。

class Solution{
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int ans = nums[1] + nums[2] + nums[3];
        for(int i = 0; i < nums.length; i++) {
            int start = i + 1, end = nums.length - 1;
            while(start < end) {
                int sum = nums[i] + nums[start] + nums[end];
                if(Math.abs(sum - target) < Math.abs(ans - target))
                ans = sum;
                if(sum > target)
                end--;
                else if(sum < target) 
                start++;
                else
                {
                    return ans;
                }
                
            }
        }
        return ans;
    }
}