numbers = [5, 6, 7, 8, 9, 10, 1, 2, 3]
def rotation (numbers):
    start , end = 0 , len (numbers) - 1
    while start < end :
        mid = start + (end - start) //  2
        if mid > 0 and numbers[mid] < numbers [mid-1]:
            return mid
        if numbers[mid] > numbers [end] :
            start = mid + 1
        else :
            end = mid 
    return start 
print (rotation(numbers)) 