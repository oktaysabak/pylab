
#  bubble sort
def bubble_sort(array):
    for n in range(0, len(array)):
        for i in range(0,len(array)-n-1):
            if array[i] > array[i+1]:
                # temp = array[i]
                # array[i] = array[i+1]
                # array[i+1] = temp
                # short way 
                array[i], array[i + 1] = array[i + 1], array[i]
    print('sorted array is: {}'.format(array))
array = [13, 3, 78, 5, 1, 34, 56, 7]
print('our array is: {}'.format(array))
bubble_sort(array)