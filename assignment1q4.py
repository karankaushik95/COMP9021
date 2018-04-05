# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 11:00:34 2018

@author: Karan
"""
'''
Write a program, stored in a file named nonredundant.py, that performs the following task.
• The program prompts the user to input a file name. If there is no file with that name in the working
directory, then the program outputs an (arbitrary) error message and exits.
• The contents of the file consists of lines with text of the form R(m,n) where m and n are integers (that just
represent labels), with possibly spaces before and after the opening and closing parentheses, respectively.
It represents a partial order relation R (so an asymmetric and transitive binary relation). For instance,
the contents of the file partial_order_1.txt can be represented as:
3 5 2 1
4
It can be seen that two facts are redundant:
{ the fact R(3; 1), which follows from the facts R(3; 5), R(5; 2) and R(2; 1);
{ the fact R(4; 1), which follows from the facts R(4; 2) and R(2; 1).
• The program outputs the facts that are nonredundant, respecting the order in which they are listed in
the file.
Here is a possible interaction:
$ cat partial_order_1.txt
R(3,5)
R(4,2)
R(5,2)
R(2,1)
R(3,1)
R(4,1)
$ python3 nonredundant.py
Which data file do you want to use? partial_order_1.txt
The nonredundant facts are:
R(3,5)
R(4,2)
R(5,2)
R(2,1)
'''
import sys
import re

filename = input('Which data file do you want to use? ')
try:
    redundancy = open(filename, 'r').readlines()
except FileNotFoundError:
        print("File doesn't exist. Quitting")
        sys.exit()
        
coordinates = dict()
redundant_path = []

'''
Find out if a path already exists from the given source node to destination node
'''
def path_exists(coordinates, source, destination):
    
    if not key_exists(coordinates, source):
        return False
    else:
        if destination in coordinates[source]:
            
            return True
        else: return False
'''
Find out if the current source node has already been seen and updated into the dictionary
'''
def key_exists(coordinates, source):
    if source in coordinates:
        return True
    else:
        coordinates[source] = []
        return False
'''
Add the current destination node to the source node
'''
def add_to_paths(coordinates, source, destination):
    if not key_exists(coordinates, source):
            coordinates[source].append(destination)
    for key, value in coordinates.items():
        if key == source:
            coordinates[key].append(destination)

'''
Add the current destionation node to all paths that lead to the current source node
'''        
def update_all_paths(coordinates):
    sources = list(coordinates.keys())
    for key, value in coordinates.items():         
        for source in sources:
            if source in value:
                temp = coordinates[source]
                for items in temp:
                    if items not in value:
                        value.append(items)
'''
Function to handle certain cases of redundant nodes where a redundant node 
is found after it has already been marked as non-redundant
'''
def remove_duplicate_paths(coordinates, source, destination):
    nodes = list(coordinates.keys())
    index_of_source = []
    for index, node in enumerate(nodes):
        if destination in coordinates[node]:
            if source in coordinates[node]:                 
                index_of_source.append(node)
    return index_of_source                


'''
Populate the dictionary to find out paths from a node to another node
'''
def populate_paths(coordinates, redundancy, redundant_path):
    
    for line in redundancy:
 
        og_line = line
        line = re.sub("\D", "", line)
        if path_exists(coordinates, line[0], line[1]):
            redundant_path.append(og_line)
        
        else:      
            add_to_paths(coordinates, line[0], line[1])
            source = remove_duplicate_paths(coordinates, line[0], line[1])
          
            if source:
               
                for key in source:
    
                    redundant_thing = key+line[1]
                    for path in redundancy:
                        
                        original_line = path
                        path = re.sub("\D", "", path)
                        if redundant_thing == path:
                            
                            redundant_path.append(original_line)
                            
            update_all_paths(coordinates)
       

populate_paths(coordinates, redundancy, redundant_path)  

print("The nonredundant facts are:")

for element in redundancy:
  if element not in redundant_path:
      print(element, end = "")
