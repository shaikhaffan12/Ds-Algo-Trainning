def selection_sort(arr):
    size = len(arr) # getting the size of array

    for i in range(size):   # outer loop for iterating through element in array
        min_index = i   # taking first index as a minimum index

        for j in range(min_index+1,size):   # inner loop start with second index because we have to compare 
            # first index with second index
            if arr[j]<arr[min_index]:   # condition for getting minimum index 
                min_index=j # if satisfies upper condition then minimum index will be change

        if arr[i] != min_index: # if element is not equals to minimum index then
            arr[i],arr[min_index]=arr[min_index],arr[i] # swap the element
    return arr

arr = [50,10,60,20,40,90,100,-1]
print(selection_sort(arr))