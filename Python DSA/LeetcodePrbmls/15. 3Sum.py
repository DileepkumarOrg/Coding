"""nums = [-1,0,1,2,-1,-4]
l=[]
for i in range(len(nums)-1):
    l1=[]
    for j in range(i+1,len(nums)-1):
        temp = -(nums[i] + nums[j])
        if temp in nums and nums.index(temp) != i and nums.index(temp) != j:
            l1.append(nums[i])
            l1.append(nums[j])
            l1.append(temp)
    l.append(l1)
print(l)"""



nums = [-1,0,1,2,-1,-4]
l=[]
for i in range(len(nums)-1):
    l1=[]
    for j in range(i+1,len(nums)-1):
        temp = -(nums[i] + nums[j])
        if temp in nums and nums.index(temp) != i and nums.index(temp) != j:
            print(nums[i], nums[j], temp)
            print(i,j,nums.index(temp))
            """nums.remove(nums[i])
            nums.remove(nums[j])
            nums.remove(-temp)"""
