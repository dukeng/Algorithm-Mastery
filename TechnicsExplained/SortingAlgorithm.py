




# Quick Sort Partition
# Partition array by a given number
def quicksortpartition(array=[9,-3,5,-2,6,4,5,-6,7,-9], index=4):
    left = 0
    right = len(array) - 2
    #swap the index to the end
    