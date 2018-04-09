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
def enclosed_by(check_rectangle, rect_dict):
    edge_count = 0
    for key,value in rect_dict.items():
        if check_rectangle == key:
            continue
        else:
            '''
            Write code to check each edge with edges in the current key.........
            '''
            pass
    if edge_count == 4:
        rect_dict.pop(check_rectangle)    
    
  
'''
Standard function to implement distance formula to calculate distance between two points
'''    

def distance_formula(source_point, destination_point):
    return (sqrt((source_point[0] - destination_point[0])**2 + (source_point[1]- destination_point[1])**2))


def parse_file(rectangles):
    for rectangle_edges in rectangles:
        x1,y1,x2,y2 = rectangle_edges.split(' ')
        edge_co_ordinates = get_corner_points_of_rectangle(int(x1),int(y1),int(x2),int(y2))
        rect_dict[edge_co_ordinates] = get_all_points_of_rectangle(edge_co_ordinates) 
        #get_all_points_of_rectangle(x1,y1,x2,y2)


'''
Function to get all vertices of the rectangle
'''
def get_corner_points_of_rectangle(x1,y1,x2,y2):
    return((x1,y1), (x1,y2), (x2,y2), (x2,y1))


def get_perimeter(rectangles):
    pass


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
    else:
        if x1>x2:
            for i in range(x2,x1+1):
                line.append((i,y1))                        
        else:
            for i in range(x1,x2+1):
                line.append((i,y1)) 
    return line
             
'''
Function to get all points on the boundary of the rectangle including the vertices
'''

def get_all_points_of_rectangle(edge_coordinates):
   coordinates = []
   for i in range(0, len(edge_coordinates)):
       edge = [] 
       for j in range(i, len(edge_coordinates)):
           if edge_coordinates[i][0] != edge_coordinates[j][0] and edge_coordinates[i][1] != edge_coordinates[j][1]:
               continue
           elif edge_coordinates[i][0] == edge_coordinates[j][0]:
               edge = get_points_on_a_line(edge_coordinates[i][0], edge_coordinates[i][1], edge_coordinates[j][0], edge_coordinates[j][1])
           elif edge_coordinates[i][1] == edge_coordinates[j][1]:
               edge = get_points_on_a_line(edge_coordinates[i][0], edge_coordinates[i][1], edge_coordinates[j][0], edge_coordinates[j][1])
       coordinates.append(edge)    
   #print(coordinates)            
   return coordinates

parse_file(rectangles)



#test = ((-15,0), (-15,10), (5,10), (5,0))
#for key,value in rect_dict.items():
    #enclosed_by(key, rect_dict)

