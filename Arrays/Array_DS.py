'''
A Python Program to Reverse an array using Data Structure
This program donot use th reverse() in-built function 
'''

def reverseArray(arr):
    result=[]
    last=len(arr)-1
    for i in range(0,len(arr)):
        result.append(arr[last-i])
    return result

if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    res = reverseArray(arr)
    print(' '.join(map(str, res)))
    print('\n')