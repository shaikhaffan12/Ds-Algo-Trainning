
def partition(array,low,high): # the function is for getting pivot element in array
    pivot = array[high] # It takes highest value as a pivot in array
    i = low-1
    for j in range(low,high):
        if array[j]<=pivot:
            i += 1
            array[i],array[j] = array[j],array[i]
    array[i+1],array[high] = array[high],array[i+1]
    return i+1  # returns index of pivot element
def Quick_sort(array,low,high):
    if high>low:
        pi = partition(array,low,high)  # calls partition function for pivot index

        Quick_sort(array,low,pi-1)  # recursively call function 
        Quick_sort(array,pi+1,high)

array = [4,2,3,1]
Quick_sort(array,0,len(array)-1)    # provide the array, starting index and endin index to the function
print("After array Sorting :- ",array)