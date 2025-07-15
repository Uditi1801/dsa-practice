#Find the missing number from 1 to n
def find_missing_num(arr):
    n=len(arr)+1
    total_sum= n*(n+1)//2
    arr_sum=sum(arr)
    return total_sum-arr_sum
print(find_missing_num([1,2,4,6,3,7,8]))
