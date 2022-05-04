# arr = [50,10,60,20,40,90,100]

def merge_sort (arr):
    if len(arr) <= 1:   # this checks if array doesn't have any elements it return nothing
        return
    mid = len(arr)//2   # this statement finds te middle element of array
    
    l = arr[:mid]   # the array divided into left array
    
    r = arr[mid:]   # same here divided into right array

    merge_sort(l)   # recursive function to sort the left array by dividing it
    merge_sort(r)   # recursive function to sort the right array by dividing it

    two_sorted_arr(l,r,arr)   # it calls the second function  

def two_sorted_arr (a,b,arr): # this function is for merge the two sorted array
    len_a = len(a) # get the array length for first array
    len_b = len(b) # get the array length for second array
    i=k=j=0        # initialize the iterating variables with 0
    while i < len_a and j < len_b:  
        if a[i] <= b[j]:    # Comparing both the array  
            arr[k] = a[i]   # if upper condition is true then it swap the element
            k += 1 
            i += 1
        else:
            arr[k] = b[j]   # otherwise this statement will be excute 
            k += 1 
            j += 1
    # sorted_list = sorted_list + a[i:] + b[j:]

    while i < len_a:    
        arr[k] = a[i]
        k += 1
        i += 1
        
    while j < len_b:
        arr[k] = b[j]
        k += 1 
        j += 1




arr = [10,3,15,7,8,23,95,29]

merge_sort(arr)
print(arr)