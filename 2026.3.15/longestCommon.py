def longestCommonPrefix(strs):
    if not strs:                                #在Python中if not+变量 的意思是 "变量为空/不存在/是False"
        return ""
    prefix = strs[0]                            #prefix为新变量，str[0]是第一个字符
    for s in strs:                              #for in  是Python里的循环语法，意思是把数组里每一个字符串拿出来挨个处理
        while not s.startswith(prefix):         
            prefix = prefix[:-1]                # while 条件循环 与for不一样   prefix[:-1] 字符串切片  作用砍掉最后一个字符
            if not prefix:
                return ""
    return prefix


