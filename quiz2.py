# Written by Karan Kaushik and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd


try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
  
has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''    

gcd_num_den = gcd(numerator,denominator)
numerator//= gcd_num_den
denominator//= gcd_num_den

integral_part = numerator//denominator
'''
Find prime factors of the integral part of the number
'''
def find_prime_factors(denominator):
    prime_factors = []
    factor = 2
    if denominator == 1:
        return
    while denominator>1:
        if denominator%factor == 0:
            denominator =  denominator/factor
            prime_factors.append(factor)
        else:
            factor =  factor + 1
    return prime_factors        

'''
A number has a finite decimal expansion if it is modulo 10, 
i.e. if it has prime factors that are multiples of 2 and 5 i.e. multiples of 10 only.
'''
def finite_or_infinite(denominator):
    
    if denominator == 1:
        return True
    L = find_prime_factors(denominator)
    for i in L:
        if i != 2:
            if i!=5:
                return False
    return True

has_finite_expansion = finite_or_infinite(denominator)
'''
To find the recurring and nonrecurring portion of the fractional part.
Store a list of remainders, and if a certain remainder repeats, that's where the
recurring portion beings.
'''
def find_sigma_tau(numerator, denominator):
    list_of_remainders = []
    flag = True
    quotient = []
    number_of_zeroes = find_number_of_zeroes(find_prime_factors(denominator)) 
    
    while flag:
        if numerator%denominator == 0:
            flag = False
            quotient.append((numerator)//denominator)
            break
        else:
            remainder = numerator%denominator
            print(numerator, denominator, (numerator-remainder)//denominator)
           
            for element in list_of_remainders:
                
                if element == remainder:
                    flag = False
                    
          
            list_of_remainders.append(remainder)
            quotient.append((numerator-remainder)//denominator)
            numerator = remainder * 10  
    
    if quotient:
        quotient.pop(0)
    sigma = quotient[0:number_of_zeroes]
    tau = quotient[number_of_zeroes:]
    return sigma,tau
    
    print(list_of_remainders)   
     
'''
Number of leading zeroes in the fractional part
'''
def find_number_of_zeroes(prime_factors):
    no_of_2 = 0
    no_of_5 = 0
    if not prime_factors:
        return 0
    for x in prime_factors:
        if x == 2 :
            no_of_2+=1
        elif x == 5:
            no_of_5+=1
    for x in prime_factors[::-1]:
        if x == 2 or x == 5:
           prime_factors.remove(x)
    if no_of_5 > no_of_2:
        return no_of_5
    else:
        return no_of_2       

sigma, tau = find_sigma_tau(numerator, denominator)
sigma = ''.join(str(e) for e in sigma)
tau = ''.join(str(e) for e in tau)

if has_finite_expansion:
    print(f'\n{numerator*gcd_num_den} / {denominator*gcd_num_den} has a finite expansion')
else:
    print(f'\n{numerator*gcd_num_den} / {denominator*gcd_num_den} has no finite expansion')
if not tau:
    if not sigma:
        print(f'{numerator*gcd_num_den} / {denominator*gcd_num_den} = {integral_part}')
    else:
        print(f'{numerator*gcd_num_den} / {denominator*gcd_num_den} = {integral_part}.{sigma}')
else:
    print(f'{numerator*gcd_num_den} / {denominator*gcd_num_den} = {integral_part}.{sigma}({tau})*')
    
