#QUICK SORT

def sort(nums, left, right):
    if left < right:
        partition_pos = partition(nums, left, right)
        sort(nums, left, partition_pos - 1)
        sort(nums, partition_pos + 1, right)
def partition(nums, left, right):
    i = left
    j = right - 1
    pivot = nums[right]
    print(pivot)

    while i < j:
        while i < right and nums[i] < pivot:
            i += 1
        while j > left and nums[j] >= pivot:
            j -= 1
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    if nums[i] > pivot:
        nums[i], nums[right] = nums[right], nums[i]
    print(nums)

    return i

nums = [61,45,97,59,25,16,62,72,48,65]
print("-----------------------QUICK SORT----------------------")
print("Unsorted List:", nums)
print( )
sort(nums, 0, len(nums) - 1)
print( )
print("Sorted List:",nums)