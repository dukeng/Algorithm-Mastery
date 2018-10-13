from random import randint





# Quick Sort Partition
# Partition array by a given number
# print(quicksortpartition([5,2,1,4,6,7,3,9,8], 4))
# print(quicksortpartition([5,2], 0))
# Swap index to the end. Use 2 pointers left and right to swap until they meet
def quicksortpartition(array=[9,-3,5,-2,6,4,5,-6,7,-9], index=4):
    if len(array) == 1:
        return array, 0
    left = 0
    right = len(array) - 2
    #swap the index to the end
    array[index], array[len(array) - 1] = array[len(array) - 1], array[index]
    compare_value = array[len(array) - 1]
    while left <= right:
        if array[left] < compare_value:
            left += 1
        else:
            array[left], array[right] = array[right], array[left]
            right -= 1
    #swap the index back to left
    array[left], array[len(array) - 1] = array[len(array) - 1], array[left]
    return array, left

def QuickSort(array=[9,-3,5,-2,6,4,5,-6,7,-9]):
    if len(array) <= 1:
        return array
    pivot = randint(0, len(array) - 1)
    newArray, newPivot = quicksortpartition(array, pivot)
    leftArray = QuickSort(newArray[:newPivot])
    rightArray = QuickSort(newArray[newPivot + 1:])
    return leftArray + [newArray[newPivot]] + rightArray



def merge(left, right):
    left_index = 0
    right_index = 0
    ans = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            ans.append(left[left_index])
            left_index += 1
        else:
            ans.append(right[right_index])
            right_index += 1
    if left_index < len(left):
        ans += left[left_index:]
    if right_index < len(right):
        ans += right[right_index:]
    return ans

def MergeSort(array=[9,-3,5,-2,6,4,5,-6,7,-9]):
    if len(array) <= 2:
        return sorted(array)
    left = MergeSort(array[:len(array) // 2])
    right = MergeSort(array[len(array) // 2:])
    return merge(left, right)

print(MergeSort())


