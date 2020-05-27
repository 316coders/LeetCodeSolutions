// 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

// 示例 1:

// 输入: 123
// 输出: 321
//  示例 2:

// 输入: -123
// 输出: -321
// 示例 3:

// 输入: 120
// 输出: 21
// 注意:

// 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
//解题思路：rev = rev * 10 + x % 10;这一步很关键，是为了交换输入数字x的公式，在交换完成后，还需要判断这个数字是否超出了范围。
#define isOverLength 0
int reverse(int x){
long rev = 0;

while(x !=0) {
    rev = rev * 10 + x % 10;
    x = x / 10;
}
if((int)rev != rev ) {
    return isOverLength;
}else 
return (int)rev;
}