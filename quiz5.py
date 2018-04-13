# -*- coding: utf-8 -*-
# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by Karan Kaushik and Eric Martin for COMP9021

import sys
from random import seed, randint
from copy import deepcopy


dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(dim)))

def modified_grid():
    for i in range(dim):
        print('   ', ' '.join(str(grid[i][j]) for j in range(dim)))



try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

'''
For part 1 of the question, replaces every contiguous instance of the top left element with a star
'''
def replace1_by_star(i,j,grid, count, start):
    if grid[i][j] == start:
        grid[i][j] = '*'
        count +=1
        if i!=0:
            count = replace1_by_star(i-1, j, grid, count, start)
        if i <dim -1:
            count = replace1_by_star(i+1, j, grid, count, start)
        if j!=0:
            count = replace1_by_star(i, j-1, grid, count, start)
        if j<dim - 1:
            count = replace1_by_star(i, j+1, grid, count, start) 
    return count         

count = 0

checked = 0

'''
To flip the current "top left" element for the purpose of checkered grid counting
'''
def zero_or_one(element):
    if element:
        return 0
    else:
        return 1

'''
Function to calculate checkered portion 
'''
def checkers(i,j,grid, checked, start):
    if grid[i][j] == start:
        grid[i][j] = '*'
        checked +=1
        
        if i:
            checked = checkers(i-1, j, grid, checked, zero_or_one(start))
                        
        if i < dim -1:
            checked = checkers(i+1, j, grid, checked, zero_or_one(start))
                        
        if j:
            checked = checkers(i, j-1, grid, checked, zero_or_one(start))
                           
        if j< dim - 1:
            checked = checkers(i, j+1, grid, checked, zero_or_one(start))              
    return checked

copy_of_grid = deepcopy(grid)

'''
Function to iterate over the whole grid to get maximum possible checkered size 
'''
def check_checks(grid):
    max_checked = 0
    checked = 0
    for i in range(0, dim-1):
        for j in range(0, dim-1):
            
            current = checkers(i, j, grid, checked, grid[i][j])
            
            if current > max_checked:
                max_checked = current
            grid = deepcopy(copy_of_grid)
            checked = 0
    
    return max_checked

checked = check_checks(grid)
            
#print(checked)

grid = deepcopy(copy_of_grid) 
size_of_largest_homogenous_region_from_top_left_corner  = replace1_by_star(0,0,grid,count, grid[0][0])

# Replace this comment with your code
print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
     )

max_size_of_region_with_checkers_structure = check_checks(grid)
# Replace this comment with your code
print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
     )
