{
    "title": "4 Sum",
    "source": "http://www.techiedelight.com/4-sum-problem/",
    "topic": "Array",
    "tags": "SubSet",
    "technics" : "Two Sum",
    "input": "arr = [ 2, 7, 4, 0, 9, 5, 1, 3]",
    "output": "Output: (0, 4, 7, 9), (1, 3, 7, 9), (2, 4, 5, 9)"
    "solution": "Go through a nested loop (index i and j) and maintain a hashMap containing all possible two sum. As we go check if the remaining sum is in the hashMap. After that need to verify that i and j is different from the sum that we see"
    "runtime" : "O(n^3), O(n^2)"

}