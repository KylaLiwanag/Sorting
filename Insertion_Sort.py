#INSERTION SORT

def sort(nums):
    for i in range(1,len(nums)):
        j = i
        while nums[j-1] > nums[j] and j > 0:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
            print(nums)

nums = [61,45,97,59,25,16,62,72,48,65]
print("---------------------INSERTION SORT--------------------")
print("Unsorted List:", nums)
print( )
sort(nums)
print( )
print("Sorted List:",nums)