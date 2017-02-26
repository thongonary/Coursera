import argparse

def get_median(one, two, three):
    mylist = [one, two, three]
    for i in mylist:
        if i is not min(mylist) and i is not max(mylist): return i 

def partition(A, left, right, pivot_type):
    # Input corresponds to A[left..right].
    # Outcome: partitioned array
    # Return: index of the pivot in the partitioned array
    partition.counter += (right - left) # Count the number of comparisons
    if debug: 
        print('   -- In partition: A = %s. Left = %d, Right = %d' %(A,left,right))
        print('   -- Adding %d to count. ' %(right-left))
    if pivot_type == 0: # pivot as the first element 
        p = A[left]
    elif pivot_type == 1: # pivot as the last element
        p = A[right]
        A[right], A[left] = A[left], A[right] # move the pivot to the first element before doing partition
    else: # pivot as the median(first, last, middle)
        if right - left < 2: # no median
            p = A[left]
        else:
            p = get_median(A[left], A[right], A[int(left+(right-left)/2)])
        if debug:
            print('Left = A[%d] = %d. Right = A[%d] = %d. Middle = A[%d] = %d' % (left, A[left], right, A[right], int(left+(right-left)/2), A[int(right-left)/2]))
            print('Pivot = %d' % p)
        if p == A[right]: A[right], A[left] = A[left], A[right]
        elif p == A[int(left+(right-left)/2)]: A[int(left+(right-left)/2)], A[left] = A[left], A[int(left+(right-left)/2)]
    i = left+1
    if debug: 
        print('   -- Pivot = %d' % p)
        print('   -- List before swap: %s' % A)
    for j in range(left+1, right+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j] # A very pythonic swapping 
            i += 1
    A[left], A[i-1] = A[i-1], A[left]
    if debug:
        print('   -- List after swap: %s' % A)
        print('   -- Split: A[%d] = %d' % (i-1,A[i-1]))
    return i-1

def quick_sort(A, left, right, pivot_type=0):
    if left >= right: return A
    if debug: print('In quick_sort: A = %s. Left = %d, Right = %d. Count = %d'% (A,left,right,partition.counter))
    split = partition(A, left, right, pivot_type)
    if debug: print('In quick_sort: Split = %d' % split)
    quick_sort(A, left, split-1, pivot_type)
    quick_sort(A, split+1, right, pivot_type)
    return A

parser = argparse.ArgumentParser(description='Quicksort using 3 types of pivot.')
parser.add_argument('--type', help = 'Specify type of pivot. 0 = First element as pivot. 1 = Last element as pivot. 2 = Median of (first, last, middle) element as pivot', required = True)
parser.add_argument('-v','--verbose', action='store_true', help = 'Print verbose for debugging.') 
parser.add_argument('-t','--test', help = 'Run test case (10, 100, 1000).')
args = parser.parse_args()

if args.test is not None:
    infile = args.test+'.txt'
else:
    infile = 'QuickSort.txt'
with open(infile) as fin:
    if args.test is not None: ele = fin.read().split('\n')
    else: ele = fin.read().split()
    int_ele = [int(i) for i in ele]
    partition.counter = 0
    debug = args.verbose
    if debug:
        print('Pivot type: %d' % int(args.type))
        print('Unsorted: %s' % int_ele)
        print('Sorted: %s' % quick_sort(int_ele, 0, len(ele)-1, int(args.type)))
    else:
        quick_sort(int_ele, 0, len(ele)-1, int(args.type)) 
    print('Number of comparisons: %d' % partition.counter)

if args.test is not None:
    print('Correct answer:\nSize First Last Median\n10 25 29 21\n100 615 587 518\n1000 10297 10184 8921')
