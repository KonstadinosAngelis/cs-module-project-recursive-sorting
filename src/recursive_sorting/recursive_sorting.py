# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []
    a_idx, b_idx = 0,0 

    while a_idx < len(arrA) and b_idx < len(arrB):
        if arrA[a_idx] < arrB[b_idx]:
            merged_arr.append(arrA[a_idx])
            a_idx+=1
        else:
            merged_arr.append(arrB[b_idx])
            b_idx+=1
    if a_idx == len(arrA): 
        merged_arr.extend(arrB[b_idx:])
    else: 
        merged_arr.extend(arrA[a_idx:])
        
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    if len(arr) > 1:
        # print(arr)
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        a = merge_sort(left)
        b = merge_sort(right)
        return merge(a,b)

    return arr

def merge_sort_in_place(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort_in_place(left)
        merge_sort_in_place(right)

        arr.clear()
        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)
        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
