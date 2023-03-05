# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    tree = {}
    rootIndex = 0
    for k in range(n):
        tree[k]=[]
    for k, par in enumerate(parents):
        par = parents[k]
        if par != -1:
           tree[par].append(k)
        else:
            rootIndex = k
    findBranch = [(rootIndex,1)]
    max_height = 0
    while findBranch:
        node, height = findBranch.pop()
        max_height = max(max_height,height)
        element = tree[node]
        for ch in element:
            findBranch.append((ch, height+1))
    # Your code here
    return max_height


def main():
    # implement input form keyboard and from files
    letter = input()
    if "F" in letter:
        fileName = input()
        if "a" in fileName:
            return
        with open(f"./test/{fileName}", mode="r") as file:
            number = int(file.readline())
            values = list(map(int, file.readline().split())) 
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
