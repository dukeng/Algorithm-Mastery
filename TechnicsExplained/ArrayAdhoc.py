

# Majority Element: find if exist an element in an array that appears N/2 + 1 times where N is the size of the array/

def MajorityElement(array):
    if not array:
        return None
    current_count = 1
    current_elem = array[0]
    for i in array[1:]:
        if i == current_elem:
            current_count += 1
        else:
            current_count -= 1
            if current_count < 0:
                current_count = 0
            current_elem = i
    if current_count > 0:
        return current_elem
    else:
        return None

print(MajorityElement([1,2,2,1,4,5,1,1]))
