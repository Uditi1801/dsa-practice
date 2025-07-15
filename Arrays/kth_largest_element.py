#finding the kth largest element
def largest_element(arr,k):
    arr.sort(reverse=True)
    return arr[k-1]
print(largest_element([5,8,91,56,87],3))
# if we want to find the second largest element but want a better time complexity
def second_largest(arr):
    if len(arr)<2:
        return None
    largest=second=float(-'inf')
    for num in arr:
        if num>largest:
            second=largest
            largest=num
        elif largest>num>second:
            second=num
