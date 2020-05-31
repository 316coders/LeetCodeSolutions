
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
解题思路：

char * longestCommonPrefix(char ** strs, int strsSize){
    if(strsSize==0) {
        return "";                                      //如果字符串数组为空，直接返回""
    }
    for(int i = 0;i < strlen(strs[0]); i++) {          //i表示列，strlen(strs[0])表示第一个字符串长度      
        for(int j = 1; j < strsSize; j++ ) {             //j表示行
            if(strs[0][i] !=strs[j][i]) {           //如果比较字符串的第i列不同，该列结束，直接跳出
                strs[0][i] = '\0';
                break;
            }
        }
    }
    return strs[0];
}