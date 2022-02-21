# Define a function that takes one integer argument and returns logical value true or false depending on if the integer is a prime.

# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.
# Requirements

#     You can assume you will be given an integer input.
#     You can not assume that the integer will be only positive. You may be given negative numbers as well (or 0).
#     NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 (or similar, depends on language version). Looping all the way up to n, or n/2, will be too slow.

from math import sqrt

def is_prime(num):
    prime_flag = 0
    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            if (num % i) == 0:
                prime_flag = 1
                break
        if prime_flag == 0:
            return True
        else:
            return False

    else:
        return False
  
