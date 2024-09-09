# Task 1: Write a program to sort a list of integers using merge sort.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half,right_half)

def merge(left,right):
    sorted_array = []
    left_index =0
    right_index =0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index +=1
        else:
            sorted_array.append(right[right_index])
            right_index +=1

# now,add remaining elements from left to right

    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    return sorted_array

numbers = [38,34,67,2,9,23,11,55]
sorted_numbers=merge_sort(numbers)
print("Sorted List: ",sorted_numbers)