"""
This file is intended to demonstrate the benefit of modular coding. I'm also 
demonstrating the first examples of docstrings in it. Look how pretty I am. 
"""

from random import randint

def rand_generator(a, b, n):
    """
    Parameters
    ----------
    a : int
        This integer is used as the lower bound for the randint() function 
        from the random library.
    
    b : int
        This integer is used as the upper bound for the randint() function 
        from the random library
        
    n : int
        This integer is used in the range() function. It is the total number 
        of random integers we wanted to generate.
    
    
    Returns
    -------
    rand_list : list
        This contains the `n` random integers between the values `a` and `b`
    """
    rand_list = [] 
    for _ in range(n):
        rand_val = randint(a, b)
        rand_list.append(rand_val) 
    return rand_list


def calc_average(some_list):
    """
    Parameters
    ----------
    some_list : list
        This is a list of numeric values.
    
    
    Returns
    -------
    avg : float
        The average of the values in the numeric list some_list.
    """
    avg = sum(some_list)/len(some_list)
    return avg


def calc_stdev(my_list):
    """
    Parameters
    ----------
    my_list : list
       A list of numeric values.
    
    Returns
    -------
    stdev : 
    """
    avg_val = sum(my_list)/len(my_list)
    diff_sqr = []
    for i in my_list:
        val = (i - avg_val)**2.0
        diff_sqr.append(val)
    stdev = (sum(diff_sqr)/len(diff_sqr))**0.5
    return stdev


def main():
    """
    Runs the random number generation, average calculation and stdev 
    calculation. No non-exit code returns for this function. Will be 
    executed if the script is run at command line.
    """
    my_rands = rand_generator(10, 70, 200)
    my_avg = calc_average(my_rands)
    my_stdev = calc_stdev(my_rands)
    print(my_avg)
    print(my_stdev)
    return 0


if __name__ == "__main__":
    main()
