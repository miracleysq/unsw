import sys
from math import sqrt


def f(n):
    '''
    Won't be tested for n greater than 10_000_000
    
    >>> f(3)
    The largest prime strictly smaller than 3 is 2.
    >>> f(10)
    The largest prime strictly smaller than 10 is 7.
    >>> f(20)
    The largest prime strictly smaller than 20 is 19.
    >>> f(210)
    The largest prime strictly smaller than 210 is 199.
    >>> f(1318)
    The largest prime strictly smaller than 1318 is 1307.
    '''

    
    if n <= 2:
        sys.exit()
    largest_prime_strictly_smaller_than_n = 0
    # Insert your code here
    num = n
    while True:
        num -= 1
        for i in range(2,int(sqrt(num))+1):
            if num % i == 0:
                break
        else:
            largest_prime_strictly_smaller_than_n = num
            break
    print(f'The largest prime strictly smaller than {n} is {largest_prime_strictly_smaller_than_n}.')

if __name__ == '__main__':
    import doctest
    doctest.testmod()
