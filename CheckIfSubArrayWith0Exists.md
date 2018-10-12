{
    "title": "Check if a subarray with sum = 0 exists in an array",
    "source": "http://www.techiedelight.com/check-subarray-with-0-sum-exists-not/",
    "topics": "Array" ,
    "tags": "Subarray" ,
    "technics": "Running Sum, Hashmap, Hashset", 
    "input" : "arr = [1,2,4,6,3,-3,-6,6,-3]",
    "output": "yes because [6,3,-3,-6]",
    "solution": "do a running sum hashMap with {key: running sum, value: index} for the array while checking if current_sum == 0 or current_sum exists in the hashMap. To find all subarray, store the value as a list of indexes.",
    "runtime": "O(n), O(n)",
    "note:" : "" 
}