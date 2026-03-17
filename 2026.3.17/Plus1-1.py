def plusOne(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):   #range(开始, 结束, 步长) 是“左闭右开”的     如果写成  range(n-1, 0, -1) ，那就只会走到1就停了，根本不会去检查第 0 位
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0              #不满足小于9，直接变为0
    return [1] + digits            #在 Python 中， +  号对列表（数组）来说代表拼接。    [1] ：这是一个只有一个元素 1 的新列表。  + digits ：把处理好的、全是 0 的列表接在后面。
