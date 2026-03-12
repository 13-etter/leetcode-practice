def twoSum(nums,target):
    #直接解法  两个for循环 缺点：时间复杂度O(n**2)
    for i in range(len(nums)):
        '''len(nums):求列表nums有多少个数字     range(len(nums))生成一串数字:0,1,2(总数减一)'''
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
            


def twoSum(nums,target);
    hashmap={}               #空字典，就是哈希表
    for i,num in enumerate(nums):
                             #enumerate不是下标，只是一个工具   作用自动把下标和元素一起取出来了！
        need=target-num
                             #目标数 减去  当前数
        if need in hashmap:
            return[hashmap[need],i]
                              #hashmap[need] 之前那个数的下标；i当前的数的下标
        hashmap[num]=i 
                              #当前数字和位置记进哈希表