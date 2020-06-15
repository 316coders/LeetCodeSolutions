

// 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

// 说明：本题中，我们将空字符串定义为有效的回文串。

// 示例 1:

// 输入: "A man, a plan, a canal: Panama"
// 输出: true
// 示例 2:

// 输入: "race a car"
// 输出: false

//解题思路： 记一笔 c++的几个内置函数

// islower(char c) 是否为小写字母
// isupper(char c) 是否为大写字母
// isdigit(char c) 是否为数字
// isalpha(char c) 是否为字母
// isalnum(char c) 是否为字母或者数字
// toupper(char c) 字母小转大
// tolower(char c) 字母大转小
// 代码

class Solution {
public:
    bool isPalindrome(string s) {
        string tmp;
        for (auto c : s) {
            if (islower(c) || isdigit(c))  tmp += c;
            else if (isupper(c)) tmp += (c + 32);
        }
        int i = 0, j = tmp.size() - 1;
        while (i < j) {
            if (tmp[i] != tmp[j]) return false;
            i++;
            j--;
        }
        return true;
    }
};
