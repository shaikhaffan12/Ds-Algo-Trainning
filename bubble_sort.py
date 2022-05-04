# arr = [50,10,60,20,40,90,100]
arr = [10,20,30,40,50]

size = len(arr) # taking length of array
swapped = False # this flag is use for finding if array is already swapped or not

for i in range(size): #outer loop for iterating element in array

    for j in range(size-i-1): # inner loop for sorting and swapping the element
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j] #swapping the element
            swappped = True

    if swapped == False:
        break

print(arr)