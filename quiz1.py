# Written by Karan Kaushik and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''


import sys
from random import seed, randint


try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)

L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []


M = list(L)
M.sort()
M = sorted(set(M), key=M.index)

for index,value in enumerate(M):
    if index%2==0: 
        elements_to_keep.append(value)
    
for index,value in enumerate(L):
    if value in elements_to_keep:
        L_1.append(value)
        
M = sorted(set(L), key = L.index)

for index,value in enumerate(M):
    if value in elements_to_keep:
        L_2.append(value)
    

def check_if_consecutive(L):
    temp = sorted(set(L), key = L.index)
    if max(temp) - min(temp) == len(temp)-1:
        return True 
    else:
        
        return False 
        
def sublists(s):
    length = len(s)
    for size in range(1, length + 1):
        for start in range(0, (length - size) + 1):
            yield s[start:start+size]

max_length = 0

for sublist in sublists(L):
    if check_if_consecutive(sublist):
        if len(sublist) > max_length:
            max_length = len(sublist)
            L_3 = []
            L_3 = list(sublist)
        
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
print('\nHere is L_1:')
print('  ', L_1)
print('\nHere is L_2:')
print('  ', L_2)
print('\nHere is L_3:')
print('  ', L_3)

