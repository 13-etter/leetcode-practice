def romanToInt(s):
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = 0
    n = len(s)                                           #len(s)Python内置函数，用来求字符串s的长度，把结果存到变量n
    for i in range(n - 1):                               #range()是Python里生成一串连续整数的内置函数，用来控制循环次数
        if roman_map[s[i]] < roman_map[s[i+1]]:          #字符串索引 s[1]为正向索引    s[-1]为反向索引
            res -= roman_map[s[i]]                       
        else:
            res += roman_map[s[i]]
    res += roman_map[s[-1]]                              #s[-1]这里是指最后一个字符
    return res