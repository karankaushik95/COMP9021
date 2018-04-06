# -*- coding: utf-8 -*-
"""
Write a program, stored in a file named triangle.py, that performs the following task.
• The program prompts the user to input a file name. If there is no file with that name in the working
directory, then the program outputs an (arbitrary) error message and exits.
• The contents of the file consists of some number of lines, each line being a sequence of integers separated
by at least one space, with possibly spaces before and after the first and last number, respectively, the
Nth line having exactly N numbers. For instance, the contents of the file triangle_1.txt can be
displayed as follows.
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
• The program outputs:
{ the largest value than can be obtained by summing up all numbers on a path that starts from the
top of the triangle, and at every level down to the penultimate level, goes down to the immediate
left or right neighbour;
{ the number of paths that yield this largest value;
{ the leftmost such path, in the form of a list.
Here is a possible interaction:
$ cat triangle_1.txt
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
$ python3 triangle.py
Which data file do you want to use? triangle_1.txt
The largest sum is: 30
The number of paths yielding this sum is: 1
The leftmost path yielding this sum is: [7, 3, 8, 7, 5]
$ cat triangle_2.txt
1
2 2
1 2 1
2 1 1 2
1 2 1 2 1
2 1 2 2 1 2
$ python3 triangle.py
Which data file do you want to use? triangle_2.txt
The largest sum is: 10
The number of paths yielding this sum is: 6
The leftmost path yielding this sum is: [1, 2, 1, 2, 2, 2]

"""

"""Written by Karan Kaushik for COMP9021"""


import sys
from copy import deepcopy

filename = input('Which data file do you want to use? ')
try:
    triangles = open(filename, 'r').readlines()
except FileNotFoundError:
        print("File doesn't exist. Quitting")
        sys.exit()

path = [] 

'''
Function to find the largest path, the leftmost path that leads to the largest path
 and the number of paths that lead to the largest path
'''
def find_best_path(path, element, range_number, next_level_path):
   
    maximum = -9999999
    ele = None
    element = int(element)
    number = 1
    
    for i in range(range_number, range_number + 2):
        if element + path[i][0] > maximum:
            ele = i
            maximum = element + path[i][0]
        elif element + path[i][0] == maximum:
            number = path[i][2] + path[i-1][2]
    
    new_path = deepcopy(path[ele][1]) 
    new_path.append(element)
        
    next_level_path.append([maximum, new_path, number])        

'''
Read from the file and process it 
'''

def populate_triangle(triangles):
    path = []
    next_level_path = []
    triangles = [x.rstrip() for x in triangles]
    triangles = [x.lstrip() for x in triangles]
    for row in reversed(triangles):
        for element in row.split(' '):
            path.append([int(element), [int(element)], 1])
        break
    for row in (reversed(triangles[:len(triangles)-1])):
        next_level_path = []
        range_number = 0
        for element in row.split(' '):
            find_best_path(path, element, range_number, next_level_path)
            range_number+=1    
        path = []
        path = deepcopy(next_level_path)
    return path            

path = populate_triangle(triangles)       

left_most_path = path[0][1]
left_most_path.reverse()

print(f'The largest sum is: {path[0][0]}')
print(f'The number of paths yielding this sum is: {path[0][2]}')
print(f'The leftmost path yielding this sum is: {left_most_path}')
