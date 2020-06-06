

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"



char * addBinary(char * a, char * b){
    int carry = 0;
	int length = (strlen(a)>strlen(b)? strlen(a)+2:strlen(b)+2);  // strlen("abc")返回3
	char* result = (char*)malloc(sizeof(char)*length);
	result[length-1] = '\0';    // 字符串结束标志
	for(int i = strlen(a)-1,j = strlen(b)-1,k = length -2; (i >=0)||(j >= 0); i--,j--,k--)
	{
		int sum = carry;
		sum += (i >= 0? a[i]-'0':0);
		sum += (j >= 0? b[j]-'0':0);

		carry = sum /2;
		result[k] = '0'+ sum % 2;
	}
	result[0] = carry+'0';
	if(carry == 0){
        for(int i = 0; i < length-1; i++)
            result[i] = result[i+1];
    }
	return result;
}
