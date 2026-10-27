'''Write a function find_extremes(nums) that returns the largest and smallest numbers in a list.

~ Don’t use max(), min(), or sorted()
~ Use a single loop
~ Handle an empty list by returning None
Input:  [4, 9, -2, 15, 7]
Output: (15, -2)'''

def find_extremes(nums):
    largest = nums[0]
    smallest = nums[0]
    
    for n in nums:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n
    
    return (largest, smallest)
lst = [1,4,9,116,0,-2,15,7]
(l,s) = find_extremes(lst)
print("Largest:", l)
print("Smallest:", s)