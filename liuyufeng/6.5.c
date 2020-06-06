

// 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。

//  

// 示例 1：

// 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
// 输出：[1,2,3,6,9,8,7,4,5]
// 示例 2：

// 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
// 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
//  

// 限制：

// 0 <= matrix.length <= 100
// 0 <= matrix[i].length <= 100


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* spiralOrder(int** matrix, int matrixSize, int* matrixColSize, int* returnSize){
    if (matrix == NULL || matrixSize == 0) {
        *returnSize = 0;
        return NULL;
    }

    *returnSize = matrixSize * matrixColSize[0];
    int *res = calloc(*returnSize, sizeof(int));

    int i = 0;
    int urow, rcol, drow, lcol, r, c;
    urow = -1;
    lcol = -1;
    drow = matrixSize;
    rcol = matrixColSize[0];

    while (i < *returnSize) {
        //right
        r = urow + 1;
        for (c = lcol + 1; i < *returnSize && c < rcol; c++) {
            res[i] = matrix[r][c];
            i++;                        //把第一行的遍历一遍
        }
        urow++;

        //down
        c = rcol - 1;
        for (r = urow + 1; i < *returnSize && r < drow; r++) {
            res[i] = matrix[r][c];
            i++;
        }
        rcol--;

        //left
        r = drow - 1;
        for (c = rcol - 1; i < *returnSize && c > lcol; c--) {
            res[i] = matrix[r][c];
            i++;
        }
        drow--;

        //up
        c = lcol + 1;
        for (r = drow - 1; i < *returnSize && r > urow; r--) {
            res[i] = matrix[r][c];
            i++;
        }
        lcol++;
    }

    return res;
}
