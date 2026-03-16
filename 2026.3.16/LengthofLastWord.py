def lengthOfLastWord(s: str) -> int:   
    length = 0
    i = len(s) - 1                           # len(s)计算字符串长度  i就像一个指针，现在它站在最后的位置
    while i >= 0 and s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    
    return length