#include <iostream>
#include <string>
#include <algorithm> 
using namespace std;

string addBinary(string a, string b) {
    int i = a.size() - 1; 
    int j = b.size() - 1;                            //int i和j 是用来遍历字符串的下标
    int carry = 0;             
    string res;           

    while (i >= 0 || j >= 0 || carry > 0) {
        int numA = (i >= 0) ? (a[i] - '0') : 0;       //把真正字符里面的‘0’，‘1’转为真正的整数    ASCII码
        int numB = (j >= 0) ? (b[j] - '0') : 0;
        int sum = numA + numB + carry;
        res.push_back( (sum % 2) + '0' );                //数字字符 =整数+‘0’   push_back在后面追加一个字符
        carry = sum / 2;
        i--;
        j--;
    }
    reverse(res.begin(), res.end());          // 反转

    return res;
}

int main() {
    string a1 = "11", b1 = "1";
    cout << a1 << " + " << b1 << " = " << addBinary(a1, b1) << endl;
    string a2 = "1010", b2 = "1011";
    cout << a2 << " + " << b2 << " = " << addBinary(a2, b2) << endl;
    string a3 = "0", b3 = "0";
    cout << a3 << " + " << b3 << " = " << addBinary(a3, b3) << endl;

    return 0;
}
