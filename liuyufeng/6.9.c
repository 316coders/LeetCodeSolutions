
// 给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

//  

// 说明:

// 初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。
// 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
//  

// 示例:

// 输入:
// nums1 = [1,2,3,0,0,0], m = 3
// nums2 = [2,5,6],       n = 3

// 输出: [1,2,2,3,5,6]



void merge(int* nums1, int nums1Size, int m, int* nums2, int nums2Size, int n){
    int *nums3 = (int *)malloc(sizeof(int) * (m + n));
    int i = 0,j = 0,x = 0;
    while(i < m && j < n)
    {
        if(nums1[i] <= nums2[j])
        {
            nums3[x] = nums1[i];
            i++;
        }
        else
        {
            nums3[x] = nums2[j];
            j++;
        }
        x++;
    }
    if(i == m && j < n)
    {
        while(j < n)
        {
            nums3[x] = nums2[j];
            j++;
            x++;
        }
    }
    if(j == n && i < m)
    {
        while(i < m)
        {
            nums3[x] = nums1[i];
            i++;
            x++;
        }
    }
    for(i = 0;i < nums1Size;i++)
    {
        nums1[i] = nums3[i];
    }
    
}

