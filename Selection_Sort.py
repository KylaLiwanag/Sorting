#SELECTION SORT

def sort(nums):
    for i in range(9):
        minpos = i
        for j in range(i,10):
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)

nums = [61,45,97,59,25,16,62,72,48,65]
print("---------------------SELECTION SORT---------------------")
print("Unsorted List:", nums)
print( )
sort(nums)
print( )
print("Sorted List:",nums)