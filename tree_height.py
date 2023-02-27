# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    height = np.zeroes(n, dtype = int)
    for i in range (n):
        if parents[i]==-1:
            height[i]=1
        else:
            height[i]= 1 + height[parents[i]]
    # Your code here
    return np.max(height)


def main():
    # implement input form keyboard and from files
    letter = input()
    if "F" in letter:
        fileName = input()
        if "a" in fileName:
            print("Enter a file name without letter 'a'")
        with open("./test/16", mode = "r") as file:
            number = int(file.readLine().strip())
            values = list(map(int, file.readLine().strip().split())) 
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    if "I" in letter:
        number = int(input())
        values = list(map(int, input().split()))
    print(compute_height(number, values))
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
