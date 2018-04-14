'''Write a program, stored in a file named perimeter.py, that performs the following task.
â€¢ Prompts the user to input the name of text file assumed to be stored in the working directory. We
assume that if the name is valid then the file consists of lines all containing 4 integers separated by
whitespace, of the form x1 y1 x2 y2 where (x1; y1) and (x2; y2) are meant to represent the coordinates
of two opposite corners of a rectangle. With the provided file frames_1.txt, the rectangles can be
represented as follows, using from top bottom the colours green, yellow, red, blue, purple, olive, and
magenta.
We assume that all rectangles are distinct and either properly overlap or are disjoint (they do not touch
each other by some of their sides or some of their corners).
â€¢ Computes and outputs the perimeter of the boundary, so with the sample file perimeter.py, the sum
of the lengths of the (external or internal) sides of the following picture.
Here is a sample run of the program with the two provided sample files.
$ python3 perimeter.py
Which data file do you want to use? frames_1.txt
The perimeter is: 228
$ python3 perimeter.py
Which data file do you want to use? frames_2.txt
The perimeter is: 9090'''

# Written by Karan Kaushik for COMP9021

import sys
from math import sqrt

filename = input('Which data file do you want to use? ')
try:
    rectangles = open(filename, 'r').readlines()
except FileNotFoundError:
        print("File doesn't exist. Quitting")
        sys.exit()

rectangles = [x.rstrip() for x in rectangles]
rectangles = [x.lstrip() for x in rectangles]

rect_dict = dict()


'''
Function to check if a rectange is completely enclosed by another rectangle,
i.e to see if it will not contribute to the perimeter(solution) at all
'''
def enclosed_by(check_rectangle, rect_dict, enclosed_rects):

    for key,value in rect_dict.items():
        if check_rectangle == key:
            continue
        else:
            top_left = key[1]
            bottom_right = key[3]
            check_left = check_rectangle[1]
            check_right = check_rectangle[3]
            if (top_left[0] < check_left[0] and check_left[0] < bottom_right[0]) and (top_left[0] < check_right[0] and check_right[0] < bottom_right[0]):
                if (top_left[1] > check_left[1] and check_left[1] > bottom_right[1]) and (top_left[1] > check_right[1] and check_right[1] > bottom_right[1]):
                    if check_rectangle not in enclosed_rects:
                        enclosed_rects.append(check_rectangle)
             
    
  
'''
Standard function to implement distance formula to calculate distance between two points
'''    

def distance_formula(source_point, destination_point):
    return int((sqrt((source_point[0] - destination_point[0])**2 + (source_point[1]- destination_point[1])**2)))


def parse_file(rectangles):
    for rectangle_edges in rectangles:
        x1,y1,x2,y2 = rectangle_edges.split(' ')
        edge_co_ordinates = get_corner_points_of_rectangle(int(x1),int(y1),int(x2),int(y2))
        rect_dict[edge_co_ordinates] = get_all_points_of_rectangle(edge_co_ordinates) 
        


'''
Function to get all vertices of the rectangle
'''
def get_corner_points_of_rectangle(x1,y1,x2,y2):
    return((x1,y1), (x1,y2), (x2,y2), (x2,y1))

'''
Finds out of a point is inside or outside a given rectangle
inside iff its x coordinate is between the x of the top left vertex and bottom right vertex
AND iff its y coordinate is between the y of bottom right vertex and top left vertex
'''
def inside_or_outside(point, rectangles):
    for key,value in rectangles.items():
        top_left = key[1]
        bottom_right = key[3]
        if top_left[0] < point[0] and point[0] < bottom_right[0]:
            if top_left[1] > point[1] and point[1] > bottom_right[1]:
                return True #implies point is inside another rectangle so you dont count the current start and end
    return False
   
'''
Function to get contributing perimeter of a rectangle
'''
def get_perimeter(edge,rectangles):
   # print(edge)
    peri = [] ##useless temporary variable
    #print(rectangles)
    current_perimeter = 0
    start = edge[0]
    #print(start)
    for item in edge:
        for key, value in rectangles.items():
            for edges in value:
                if item in edges:
                    #print("start", start)
                    #print("intersected edge", item)

                    if inside_or_outside(start, rectangles):
                        start = item
                        end = None ##means current edge portion is actually inside another rectangle  
                    else: ##now what if not eh?
                        peri.append((start, item))
                        current_perimeter += distance_formula(start, item)
                else:
                    end = item
                    
    end = edge[len(edge)-1]
    #print(start,end)
    if not inside_or_outside(end, rectangles):
        peri.append((start, item))
        current_perimeter += distance_formula(start, end) 
    #print(peri)
    return current_perimeter           
'''
There could be 2 intersections what about that? HANDLED YOOOOOOOOOOO  
'''
'''
Get all points in a line given the endpoints
'''
def get_points_on_a_line(x1 ,y1 , x2, y2 ):
    line = []
    if x1==x2:
        if y1>y2:
            for i in range(y2,y1+1):
                line.append((x1,i))
        else:
            for i in range(y1,y2+1):
                line.append((x1,i))
    elif y1==y2:
        if x1>x2:
            for i in range(x2,x1+1):
                line.append((i,y1))                        
        else:
            for i in range(x1,x2+1):
                line.append((i,y1)) 
    #print(line)
    return line
             
'''
Function to get all points on the boundary of the rectangle including the vertices
'''

def get_all_points_of_rectangle(edge_coordinates):
   coordinates = []
   #print("edges", edge_coordinates)
   for i in range(0, len(edge_coordinates)-1):
       edge = [] 
       #print("Current vertex",edge_coordinates[i][0], edge_coordinates[i][1])
       for j in range(i+1, len(edge_coordinates)):
           #print("Check vertex",edge_coordinates[j][0], edge_coordinates[j][1])
           
           if edge_coordinates[i][0] != edge_coordinates[j][0] and edge_coordinates[i][1] != edge_coordinates[j][1]:
               #print("opposite for current j")
               #print()
               continue
           elif edge_coordinates[i][0] == edge_coordinates[j][0]:
               edge = get_points_on_a_line(edge_coordinates[i][0], edge_coordinates[i][1], edge_coordinates[j][0], edge_coordinates[j][1])
               #print("x same for current j")
               #print()
           elif edge_coordinates[i][1] == edge_coordinates[j][1]:
               edge = get_points_on_a_line(edge_coordinates[i][0], edge_coordinates[i][1], edge_coordinates[j][0], edge_coordinates[j][1])
               #print("y same for current j")
               #print()
           coordinates.append(edge)    
   #print(coordinates)            
   return coordinates

parse_file(rectangles)

    
perimeter = 0
enclosed_rects = []
   



for key,value in rect_dict.items():
    enclosed_by(key,rect_dict, enclosed_rects)

for item in enclosed_rects:
    rect_dict.pop(item)

#for key,value in rect_dict.items():
   # print(key)
    #print()

for key,value in rect_dict.items():
    edges = rect_dict[key]    
    #print(l[0])
    temp_dict = dict(rect_dict)
    temp_dict.pop(key)
    #print(edges)
    for edge in edges:
        perimeter += get_perimeter(edge, temp_dict)    
    
    #call perimeter here? 
print("The perimeter is:",perimeter)
