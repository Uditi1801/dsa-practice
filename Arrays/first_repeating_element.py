#Find the first repeating element in the array
def first_repeating_element(arr):
    seen=set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None
print(first_repeating_element([1,2,2,3,4,5,5]))
