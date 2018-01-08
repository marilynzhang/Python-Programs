import random
import time
import copy
import heapq

#-------------------------------sorting algorithms-----------------------------

#big O average, worst, best case is O(N^2)
#--> but with a flag, best case is O(N)
def bubble_sort(array):
    for j in reversed(range(0, len(array))):
        flag = True
        for i in range(0, j):
            if array[i] > array[i+1]:
                swap(array, i, i+1)
                flag = False
        if flag:
            return array
    return array

#big O average, worst, best case is O(N^2)
def selection_sort(array):
    for j in range(0, len(array)):
        mini = array[j]
        minindex = j
        for i in range(j+1, len(array)):
            if array[i] < mini:
                mini = array[i]
                minindex = i
        swap(array, minindex, j)
    return array

#big O average, worst, best, case is O(N^2), O(N^2), O(N)
def insertion_sort(array):
    for i in range(0, len(array)):
        for j in reversed(range(1, i+1)):
            if array[j] < array[j - 1]:
                swap (array, j, j-1)
            else:
                break
    return array

#big O average, worst, best case: O(nlogn)
def merge_sort(array):
    if len(array) == 1:
        return array
    array1 = merge_sort(array[0:len(array)/2])
    array2 = merge_sort(array[len(array)/2:len(array)])
    s = 0
    f = 0
    temp = []
    while (f < len(array1) or s < len(array2)):
        if (f < len(array1) and (s == len(array2) or array1[f] < array2[s])):
            temp.append(array1[f])
            f += 1
        else:
            temp.append(array2[s])
            s += 1
    return temp

#big O average, worst, best case: O(nlogn), O(n^2), O(nlogn)
#--> worst case case happens when pivot is chosen as first or last element each time
def quick_sort(array):
    _quick_sort(array,0,len(array)-1)

def _quick_sort(array,l,r):
    if l < r:
        pivot = partition(array,l,r)
        _quick_sort(array, l, pivot-1)
        _quick_sort(array,pivot+1,r)

def partition(array,l,r):
    pivot = random.randint(l,r)
    swap(array,pivot,r)
    for i in range(l,r):
        if array[i] <= array[r]:
            swap(array,i,l)
            l += 1
    swap (array,l, r)
    return l

#big O average, worst, best case: O(nlogn)
# --> using our own heap implementation
def heap_sort(array):
    heapify(array)
    result = []
    while array:
        result.append(pop(array))
    return result

def heapify(array):
    for i in reversed(range(0, len(array))):
        sift_down(array,i)

def pop(array):
    swap(array,0,len(array)-1)
    popped = array[len(array)-1]
    array.pop(len(array)-1)
    sift_down(array,0)
    return popped

def sift_down(array, n):
    if 2*n+1 < len(array):
        child1 = array[2*n+1]
    else:
        return
    if 2*n+2 < len(array):
        child2 = array[2*n+2]
        mini = child1
        minindex = 2*n+1
        if child2 < child1:
            mini = child2
            minindex = 2*n+2
        if mini < array[n]:
            swap(array,n,minindex)
            sift_down(array, minindex)
        else:
            return
    else:
         if child1 < array[n]:
             swap(array, n, 2*n+1)
             sift_down(array,2*n+1)
         else:
             return

#using python's heap implementation for heap sort
def heap_sort_given(array):
    heapq.heapify(array)
    result = []
    while array:
        result.append(heapq.heappop(array))
    return result

#big O average, worst, best cases: O(n(logn)^2), O(n(logn)^2), O(nlogn)
def shell_sort(array):
    gap = len(array)/2
    while (gap>0):
        for i in range(gap, len(array)):
            j = i
            while (j - gap >= 0 and array[j-gap] > array[j]):
                swap(array,j,j-gap)
                j -= gap
        gap = gap/2
    return array

#this was our original, with j > i during the swaps. the new one (above) has
#i > j during the swaps
def shell_sort_original(array):
    gap = len(array)/2
    while (gap>0):
        for i in range(0,len(array) - gap):
            j = i + gap
            if (array[i] > array[j]):
                swap(array,i,j)
                k = i
                while (k - gap >= 0 and array[k-gap] > array[k]):
                    swap(array,k, k-gap)
                    k -= gap
        gap = gap/2
    return array

#just a helper method
def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

#testing for time each algorithm takes
def run_algs(array):
    algos = ['bubble_sort', 'selection_sort', 'insertion_sort','merge_sort','quick_sort','heap_sort','shell_sort']
    for algo_name in algos:
        array2 = list(array)
        time1 = time.time()
        exec algo_name + '(array2' + ')'
        time2 = time.time()
        timediff = time2 - time1
        print algo_name, '\t', timediff

#-----------------------------testing------------------------------------------
#test for the time each algorithm takes
array = []
for i in range(0,10000):
    array.append(random.randint(0,10000))
run_algs(array)

#test accuracy of each algorithm
array = [3,88,67,8,0,0,2,0,-1,-7]
print 'unsorted array', '\t', array
array1 = list(array)
bubble_sort(array1)
print 'bubble_sort', '\t', array1
array2 = list(array)
selection_sort(array2)
print 'selection_sort', '\t', array2
array3 = list(array)
insertion_sort(array3)
print 'insertion_sort', '\t', array3
array4 = list(array)
print 'merge_sort', '\t', merge_sort(array4)
array5 = list(array)
quick_sort(array5)
print 'quick_sort', '\t', array5
array6 = list(array)
print 'heap_sort', '\t', heap_sort(array6)
array7 = list(array)
shell_sort(array7)
print 'shell_sort', '\t', array7


#---------------------------------old testing methods--------------------------
# print array
# exec 'bubble_sort' + "(array" + ")"
# print array

# array1 = list(array)
# print "heap sort", heap_sort(array)
# print "shell sort", shell_sort(array1)
# array = [88,67,3,8,0,2,0,0,-1,-7]
# array2 = [16,4,7,23,0,-5]
# heapify(array2)
# print array2
# heapify(array)
# print array
#print "heap sort given", heap_sort_given(array)
# print "heap sort", heap_sort(array)
# print "quick sort"
# quick_sort(array)
# print array
# print "merge sort", merge_sort(array)
# print "insertion sort", insertion_sort(array)

# array = []
# for i in range(0, 10000):
#     array.append(random.randint(0,100))
# arr1 = array[:]
# arr2 = array[:]
# arr3 = array[:]
# #print "unsorted", array
#
# t1 = time.time()
# #print "bubble sort",
# bubble_sort(arr1)
# t2 = time.time()
# print "bubble sort time - unsorted array", t2 - t1
#
# t1 = time.time()
# #print "selection sort",
# selection_sort(arr2)
# t2 = time.time()
# print "selection sort time - unsorted array", t2 - t1
#
# array = []
# for i in range(0, 10000):
#     array.append(i)
# arr1 = array[:]
# arr2 = array[:]
# arr3 = array[:]
# #print "unsorted", array
#
# t1 = time.time()
# #print "bubble sort",
# bubble_sort(arr1)
# t2 = time.time()
# print "bubble sort time - sorted array", t2 - t1
#
# t1 = time.time()
# #print "selection sort",
# selection_sort(arr2)
# t2 = time.time()
# print "selection sort time - sorted array", t2 - t1


#----------------------------------old methods----------------------------------
#this method for quicksort doesn't really work but uses double whiles instead
#of a for loop.

# def partition(array,l,r):
#     if len(array) == 1:
#         return
#     pivot = random.randint(l,r)
#     while (l < r):
#         print array
#         while (l < pivot and array[l] < array[pivot]):
#             l += 1
#         while (r > pivot and array[r] > array[pivot]):
#             r -= 1
#         if l == pivot:
#             pivot = r
#         elif r == pivot:
#             pivot = l
#         swap (array, r, l)
#         if l == pivot:
#             r -= 1
#         elif r == pivot:
#             l += 1
#     return pivot
#
# def quick_sort(array, l=0, r=None):
#     if r is None:
#         r = len(array) - 1
#     if l >= r:
#         return
#     pivot = partition(array,0,len(array)- 1)
#     quick_sort(array, l, pivot -1)
#     quick_sort(array, pivot + 1, r)
#
#     #return [quick_sort(array[0:pivot]), pivotV, quick_sort(array[pivot+1:len(array)])]
