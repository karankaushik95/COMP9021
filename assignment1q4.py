# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 18:24:29 2018

@author: Karan
"""
'''
Problem Statement:
Write a program, stored in a file named fish.py, that performs the following task.
• The program prompts the user to input a file name. If there is no file with that name in the working
directory, then the program outputs an (arbitrary) error message and exits.
• The contents of the file consists of some number of lines, each line being a sequence of two nonnegative
integers separated by at least one space, with possibly spaces before and after the first and second
number, respectively, the first numbers listed from the first line to the last line forming a strictly
increasing sequence. The first number represents the distance (say in kilometres) from a point on the
coast to a fishing town further down the coast (so the towns are listed as if we were driving down the
coast from some fixed point); the second number represents the quantity (say in kilos) of fish that has
been caught during the early hours of the day by that town’s fishermen. For instance, the contents of
the file coast_1.txt can be displayed as
5 70
15 100
1200 20
which corresponds to the case where we have 3 towns, one situated 5 km south the point, a second one
situated 15 km south the point, and a third one situated 1200 km south the point, with 70, 100 and 20
kilos of fish being caught by those town’s fishermen, respectively.
• The aim is to maximise the quantity of fish available in all towns (the same in all towns) by possibly
transporting fish from one town to another one, but unfortunately losing 1 kilo of fish per kilometre. For
instance, if one decides to send 20 kilos of fish from the second town to the first one, then the second town
ends up having 100 − 20 = 80 kilos of fish, whereas the first one ends up having 70 + 20 − (15 − 5) = 80
kilos of fish too.
• The program outputs that maximum quantity of fish that all towns can have by possibly transporting
fish in an optimal way.

'''
import sys
from copy import deepcopy

cities = []  

filename = input('Which data file do you want to use? ')
try:
    fishy = open(filename, 'r').readlines()
except FileNotFoundError:
        print("File doesn't exist. Quitting")
        sys.exit()
'''
Check if current state satisfies current goal, i.e. if all cities but last have "goal" 
amount of fishes and the last city has more/less fishes than goal state to determine 
next "goal"
'''

def check_cities(cities, goal):
    #print(cities)
    for i in range(len(cities)):
        #print(cities[i][1])
        if cities[i][1] < goal:
            return False
    if cities[len(cities)-1][1] > goal:
        return True
    else:
        return False
'''
to return lower bound, i.e. minimum number of fishes in a city.
''' 

def get_minimum(cities):
    minimum = 999999
    for city in cities:
        if city[1] < minimum:
            minimum = city[1]
    return minimum        

'''
Get next goal state
'''
def binary_search(maximum, minimum):
    return (maximum+minimum)//2


'''
Read the input file and store it in a list
'''
def initialize_list(fishy):
    total_fishes = 0
    for line in fishy:
        distance, fishes = line.split(' ')
        cities.append([int(distance), int(fishes)])
        total_fishes+=int(fishes)       
    return total_fishes    

'''
Returns the amount of fish that will be lost during transport. 1 fish/km
'''
def calculate_loss_in_transport(origin, destination):
    return abs(origin-destination)

'''
Move fishes from city i+1 to city i to make it the goal state
AND
if city i has more fishes than goal state, move it to i+1 city
'''
def make_city_goal(goal, cities, current_city):
    if cities[current_city][1] < goal:
        cost = (goal - cities[current_city][1])  + calculate_loss_in_transport(cities[current_city][0], cities[current_city+1][0])
        #print("cost",cost)
        cities[current_city][1] = goal
        cities[current_city+1][1] -= cost
    if cities[current_city][1] > goal:
        transported = cities[current_city][1] - goal
        cities[current_city][1] = goal  
        cost = transported - calculate_loss_in_transport(cities[current_city][0], cities[current_city+1][0])
        if cost > 0:
            cities[current_city+1][1] += cost
        
'''
Check if goal state has been reached. Goal state occurs if one of two conditions are met
1) All cities have the same amount of fish
    OR
2) All cities have at least the goal amount of fish AND the next goal state is same as current goal state    
'''
def check_goal_state(minimum, maximum, goal_state, cities):
    
    equivalent_fish = True
    at_least_goal_fishes = True
    binary = False

    if binary_search(goal_state, maximum) == goal_state:
        binary = True
    
    for city in cities:
        if city[1] != goal_state:
            equivalent_fish = False
        if city[1] < goal_state:
            at_least_goal_fishes = False
            
    return equivalent_fish or (at_least_goal_fishes and binary)            
            
'''
Main computation of the algorithm takes place here
'''
def find_fishes(cities, total_fishes):
    minimum = get_minimum(cities)
    maximum = total_fishes//len(cities)
    current_goal = 0
    goal_not_found = True
    while goal_not_found:        
        
        current_goal = binary_search(minimum, maximum)
        
        for i in range(len(cities) - 1):
             make_city_goal(current_goal, cities, i)
        
        goal_not_found = not(check_goal_state(minimum, maximum, current_goal, cities))
        
        
        if goal_not_found:    
            if check_cities(cities, current_goal):
                minimum = current_goal
            else:
                maximum = current_goal
 
        cities = deepcopy(copy_of_cities)
              
    return current_goal    
    
total_fishes = initialize_list(fishy)     
copy_of_cities = deepcopy(cities)     

max = find_fishes(cities,total_fishes)

print(f'The maximum quantity of fish that each town can have is {max}.')




