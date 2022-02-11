def twoSum( nums,target):
        for i in range(len(nums)):
            a=nums[i];
            for j in range(i+1, len(nums)):
                b=nums[j];
                if ((a+b)==target):
                    print([i,j]);

target=9;
nums=[2,7,11,34]
twoSum(nums,target);
