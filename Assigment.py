import random
import time
import sys
sys.setrecursionlimit(5000)

def generat_random_array(size,allow_duplicate):
    if allow_duplicate == 1:
        return random.choices(range(1,50),k=size)
    else:
        return random.sample(range(1,50), size)


def iterative_isertion_sort(arr):
    comparisons =0
    swaps =0
    start_time = time.time()

    for i in range(1,len(arr)):
        key  = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j-=1
            swaps+=1
            comparisons+=1
        arr[j+1] = key
        if j >= 0 and key > arr[j] :
            comparisons += 1
        
    end_tme = time.time()
    execution_time  = end_tme - start_time
    return comparisons , swaps , execution_time


def recursive_insertion_sort(arr , i =1 , comparisons = 0, swaps = 0):
    if i< len(arr): 
        key = arr[i]
        j = i-1
        while j >= 0 and  key < arr[j] :
            arr[j+1] = arr[j] 
            j = j-1
            comparisons+=1
            swaps+=1
        arr[j+1] = key
        if j >= 0 and  key > arr[j]:
            comparisons+=1
        return recursive_insertion_sort(arr,i+1,comparisons,swaps)
    else:
        return comparisons,swaps


def print_result(arr,size,comparisons,swaps,execution_time):
    print("sorted array: ",arr if size <= 10 else "array size is too large!")
    print("Number of comparisons: ",comparisons)
    print("Number of swaps: ",swaps)
    print("Execution time: ",execution_time," seconds")


def  main():
    size = int(input("Enter the size of the array: "))
    allow_duplicate = int(input("Enter 1 if you want to allow the duplicate otherwise 0 : "))
    sorting_order = int(input("Enter 1 if you want the order ascending or 0 if you want the order descending: "))
    arr = generat_random_array(size , allow_duplicate)
    print("Random arry: ",arr if size <= 10 else "Array size too large!\n")
    if sorting_order == 1:
        arr_iterative = arr.copy()
        comparisons , swaps, execution_time = iterative_isertion_sort(arr_iterative)
        print("iterative insertion sort:") 
        print_result(arr_iterative,size,comparisons,swaps,execution_time)

        arr_recursive = arr.copy()
        start_time_recursive = time.time()
        comparisons,swaps = recursive_insertion_sort(arr_recursive)
        end_time_recursive= time.time()
        recursive_execution_time = end_time_recursive - start_time_recursive
        print("recursive insertion sort")
        print_result(arr_recursive,size,comparisons,swaps,recursive_execution_time)

    elif sorting_order == 0:
        arr_iterative = arr.copy()
        comparisons , swaps, execution_time = iterative_isertion_sort(arr_iterative)
        print("iterative insertion sort:") 
        print_result(arr_iterative[::-1],size,comparisons,swaps,execution_time)

        arr_recursive = arr.copy()
        start_time_recursive = time.time()
        comparisons,swaps = recursive_insertion_sort(arr_recursive)
        end_time_recursive= time.time()
        recursive_execution_time = end_time_recursive - start_time_recursive
        print("recursive insertion sort")
        print_result(arr_recursive[::-1],size,comparisons,swaps,recursive_execution_time)
    else:
        print("invalid sorting order,please enter 0 or 1")

main()