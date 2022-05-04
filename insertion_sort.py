def insertion_sort(arr):
    range_value = range(1,len(arr)) # getting the length of array this statement points second element because 
    # in insertion sort we assume that first element is already sorted

    # below for loop is for iterating through elements in array
    for i in range_value:
        unsorted_value = arr[i] # this statement point the second element of array which means second index of array

        while arr[i-1]> unsorted_value and i>0: # this statement means that if first element of array is 
            #greater than second element of array for first iteration then swap the element 

            arr[i-1],arr[i] = arr[i],arr[i-1] # swap method to swap elements
            i=i-1
    return arr

arr = [50,10,60,20,40,90,100,-1]
print(insertion_sort(arr))