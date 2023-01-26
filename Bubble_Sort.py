#BUBBLE SORT

def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                print(nums)
nums = [61,45,97,59,25,16,62,72,48,65]
print("----------------------BUBBLE SORT----------------------")
print("Unsorted List:", nums)
print( )
sort(nums)
print( )
print("Sorted List:",nums)