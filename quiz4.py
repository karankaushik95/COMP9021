# Uses National Data on the relative frequency of given names in the population of U.S. births,
# stored in a directory "names", in files named "yobxxxx.txt with xxxx being the year of birth.
#
# Prompts the user for a first name, and finds out the first year
# when this name was most popular in terms of frequency of names being given,
# as a female name and as a male name.
# 
# Written by Karan Kaushik and Eric Martin for COMP9021


import os
from collections import defaultdict

'''
Initialize a directory(HashMap) to store the names, genders and frequency of males and females
'''
years_by_names_female = defaultdict(list)
years_by_names_male = defaultdict(list)

first_name = input('Enter a first name: ')
directory = 'names'
min_male_frequency = 0
male_first_year = None
min_female_frequency = 0
female_first_year = None

'''
Parse the text file and store the data in the initialized dictionaries
'''
def populate_names(directory):
    for filename in os.listdir(directory):
        if not filename.endswith('.txt'):
            continue
        year = int(filename[3: 7])
        with open(directory + '/' + filename) as data_file: 
            for line in data_file:
                #extracting the fields from the lines
                name, gender, count = line.split(',')
                if gender =='M':
                    years_by_names_male[name].append([year,int(count)])
                else:
                    years_by_names_female[name].append([year,int(count)])

'''
Function to find which year a given name input by the user was the most popular among the names of the year,
and what percent of names of that year it accounted for (male)
'''

def find_percentage_of_name_male(first_name, current_year):
    sum_of_names_male= 0
    for name, year_and_frequency in years_by_names_male.items():
        for element in year_and_frequency:
            if element[0] == current_year:
                sum_of_names_male += element[1]
                
    return sum_of_names_male     

'''
Function to find which year a given name input by the user was the most popular among the names of the year,
and what percent of names of that year it accounted for (female)
'''

def find_percentage_of_name_female(first_name, current_year):
    sum_of_names_female= 0
    for name, year_and_frequency in years_by_names_female.items():
        for element in year_and_frequency:
            if element[0] == current_year:
                sum_of_names_female += element[1]
    return sum_of_names_female         

'''
Function that finds the instances of the names and sends it to the above function to find when 
it was the most popular
'''
def find_first_instance_of_names(first_name, male_first_year, female_first_year):
    max_percentage = 0
    
    first_name_in_all_of_history_male = 0
    first_name_in_all_of_history_female = 0
    
    percentage_of_male = 0
    percentage_of_female = 0
    
    if first_name in years_by_names_male:
        for year, frequency in years_by_names_male[first_name]:
            first_name_in_all_of_history_male +=frequency
            total = find_percentage_of_name_male(first_name,year)
            percentage = (frequency/total)*100
            if percentage> max_percentage:
                max_percentage = percentage
                percentage_of_male = percentage
                male_first_year = year
                    
    max_percentage_f = 0
    
    if first_name in years_by_names_female:
        for year, frequency in years_by_names_female[first_name]:
            first_name_in_all_of_history_female +=frequency
            total = find_percentage_of_name_female(first_name,year)
            percentage = (frequency/total)*100
            if percentage> max_percentage_f:
                max_percentage_f = percentage
                percentage_of_female = percentage
                female_first_year = year    
        
    return male_first_year,female_first_year,percentage_of_male,percentage_of_female     

populate_names(directory)
male_first_year, female_first_year,min_male_frequency,min_female_frequency = find_first_instance_of_names(first_name, male_first_year, female_first_year)


             
if not female_first_year:
    print(f'In all years, {first_name} was never given as a female name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a female name first in the year {female_first_year}.\n'
          f'  It then accounted for {min_female_frequency:.2f}% of all female names.'
         )
if not male_first_year:
    print(f'In all years, {first_name} was never given as a male name.')
else:
    print(f'In terms of frequency, {first_name} was the most popular '
          f'as a male name first in the year {male_first_year}.\n'
          f'  It then accounted for {min_male_frequency:.2f}% of all male names.'
         )

