# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1 
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1 
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by Karan Kaushik and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict
from copy import deepcopy


class NotTriangleException(Exception):
    pass

def create_dictionary():
    global triangles
    triangles['N'] = []
    triangles['S'] = []
    triangles['E'] = []
    triangles['W'] = []

def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def triangles_in_grid(dimension):
    #print(dim) 
    find_number_of_triangles(dimension)
    


#finds dimension-th odd number i.e. number of 1s in the base of the triangle of size dim
def find_odd_number(dimension):
    return 2 * dimension - 1
               

def time_to_blacklist(base,start,end):
    global blacklisted_nodes
    #print("got here")
    while(start!=end):
        #print("do i even get here?")
        blacklisted_nodes.append([(base,start), (base,end)])
        start+=1
        end-=1
        base-=1

    
def find_complete_triangle(row,start_col,end_col, size):
    global base_of_triangles
    global blacklisted_nodes
    start = start_col
    end = end_col
    base = row
    flag = True
    ones = 0
    for i in range(1,size+1,1): 
        ones += find_odd_number(i)
    #print(ones)
    ones -= find_odd_number(size)

    if ([(base, start),(base, end)]) in blacklisted_nodes:
    #   print("duplicate")
        flag = False
    try:
        while start_col <= end_col and flag == True:
            row-=1
            start_col+=1
            end_col-=1
            if row <0 or start_col <0 or end_col <0:
                raise NotTriangleException
            temp = end_col
            while start_col!=temp and flag == True:
                if size==5:
                    print(grid[row][temp])
                if [(row,start_col),(row,temp)] in blacklisted_nodes:
                    raise NotTriangleException
                    flag = False
                elif grid[row][temp] == 0:
                    raise NotTriangleException
                    flag = False
                #if size == 5:
                    #print(grid[row][temp], end = " ")    
                temp-=1    
                #if(grid[base][start_col]!=0):
                #   ones-=1
    except NotTriangleException:
        #print("excepted")
        flag = False
    #print(flag)    
    if(grid[base][start_col]==0):
        flag = False
    if size == 5 and flag:
       print("should be here", [(base, start),(base, end)])    
    if flag == True:
        base_of_triangles[size].append([(base,start), (base,end)])
        time_to_blacklist(base,start,end)
        
def calculate_triangles(size, dimension):
    number_of_ones = find_odd_number(size)
    if number_of_ones > dimension:
        return
    global base_of_triangles
    base_of_triangles[size] = []
    #counter = 0
    #print(number_of_ones)
    global blacklisted_nodes
    col = 0 #Useless assignment
    try:
        for i in range(dimension -1, -1, -1):
            #if i==0:
             #print(i, "debug mode")
            for col in range(0, dimension, 1):
                counter = 0
                #if i==0:
                 #   print("start column", col)
                for j in range(col, (dimension if col + number_of_ones > dimension else col+number_of_ones), 1):
                    #if col+number_of_ones> dimension -1:
                    #    break
                    #print(j)
                    #if i==0:
                     #   print("iter column", j)
                    #if grid[i][j] != 1:
                    #    continue # Do nothing cause base doesn't exist in this line. 
                    #print([(i,col)]," = ", int(grid[i][col]),[(i,j)]," = ", int(grid[i][j]))
                    if grid[i][j] != 0:
                        counter+=1
                        #if i==0:
                         #   print("counter", counter)
                            # print("here", counter)
                        if counter == number_of_ones and [(i,col),(i,j)] not in blacklisted_nodes:
                
                                find_complete_triangle(i,col, j, size)
                                #base exists from grid[i][col] to grid[i][j]
                
    except IndexError:
        print("Index Error")    
        pass
    #for key,value in base_of_triangles.items():
     #   print(key,value)
    #for key, value in base_of_triangles.items():
    #print value
    #    print(key, len([item for item in value if item]))
    #print(blacklisted_nodes)    

def find_number_of_triangles(dimension):
    current_size = dimension - 1
    while current_size>1:
        calculate_triangles(current_size, dimension)
        current_size -=1
        

def regenerate_grid():
    global grid
    global copy_of_grid
    grid = deepcopy(copy_of_grid)  #Most likely redundant function as grid modification is frowned upon
    
    
def copygrid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(copy_of_grid[i][j] != 0)) for j in range(len(grid)))) #Redundant function    

# Possibly define other functions

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
copy_of_grid = deepcopy(grid)

triangles = defaultdict(lambda: defaultdict(int))
create_dictionary()

base_of_triangles = dict()
blacklisted_nodes = list()

#calculate_triangles(2,3)
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles_in_grid(dim)
for key, value in base_of_triangles.items():
    #print value
    print(key, len([item for item in value if item]))

#calculate_triangles(2, 11)
'''triangles = triangles_in_grid(dim)
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')'''
