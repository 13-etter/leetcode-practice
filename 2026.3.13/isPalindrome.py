         #转字符串反转
def isPalindrome(x:int)->bool:
                 #isPalindrome 是函数名，意思是 是回文数吗？
                 #x:int  参数x为整数类型
                 #->bool  函数返回布尔值
    if x<0 or(x!=0 and x%10==0):
        return False 
    s=str(x)
                 #s是我们定义的新变量  把x转换成字符串(str)存进去  
                 #把整数x转为字符串类型，比如“121”  转为“121”
    return s==s[::-1]
                 #Python字符串语法，从后往前取整个字符串，也就是反转  例 "121"[::-1]->"121"    "123"[::-1]->"321"
                 #比较原字符串和反转后是否相同  相同： 返回 True  不相等：返回False




         #数学反转  
def isPalindrome(x:int)->bool:
    if x<0 or(x!=0 and x%10==0):
        return False 
    reversed_num=0
                 #存储我们从x末尾取出来，反转得到的数字 设置初始值0
    while x>reversed_num:
        reversed_num=reversed_num*10+x%10               
        x=x//10
                 #第一次循环  x%10=1 reversed_num=0*10+1=1 x=1221//10=122
                 #第二次循环  x%10=2 reversed_num=1*10+2=12 x=122//10=12
    return x==reversed_num or x==reversed_num//10   #x为奇数也不能落下            