import time
import csv
from math import sqrt, ceil
from random import randint, randrange
from fractions import gcd
from itertools import chain, cycle
from pyecm import factors

# prechosen list of numbers to avoid unecessary complexity from unique cases, i.e. n = 1
primes = [(3,5), (59,73), (563,859), (2053,9371), (10771,63463), (123449,984539), (4352377,9134617),
          (12454679,97665457), (276654563,976654579), (2766545629,6578494243), (12987435733,92987435687),
          (129871435667, 99871435679), (1239831093799,8739831093839), (21739831093829,71739831093841),
          (311739831093811,911739831093691)]

composites = [(2,4), (56,74), (524,834), (2034,9536), (10348,63352), (123522,984532), (4352333,9135762),
              (12454676,97665456), (276654562,976654562), (2766545627,6578494231), (12987435667,92987435667),
              (129871435662,999871435667), (1239831093821,8739831093821), (21739831093821,71739831093821),
              (311739831093821,911739831093721)]

bounds = [9, 99, 999, 9999, 99999, 999999, 9999999, 99999999, 999999999]              
              
def primetimer(func):
    rows = [['Magnitude', 'Time (sec)']]
    path = r'C:\Users\Kenny\Dropbox\BCA\Senior Year\EE\%s_prime.csv'%func.__name__
        
    for i in range(len(primes)):
        start = time.clock()
        for j in range(10):
            func(primes[i][0])
            func(primes[i][1])
        t = time.clock() - start
        row = [i, t]
        print(row)
        rows.append(row)
        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def comptimer(func):
    rows = [['Magnitude', 'Time (sec)']]
    path = r'C:\Users\Kenny\Dropbox\BCA\Senior Year\EE\%s_composite.csv'%func.__name__
        
    for i in range(len(composites)):
        start = time.clock()
        for j in range(10):
            func(composites[i][0])
            func(composites[i][1])
        t = time.clock() - start
        row = [i, t]
        print(row)
        rows.append(row)
        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)      

def primesievetimer(func):
    rows = [['Magnitude', 'Time (sec)']]
    path = r'C:\Users\Kenny\Dropbox\BCA\Senior Year\ToK\%s_prime.csv'%func.__name__
        
    for i in range(len(primes[:9])):
        start = time.clock()
        for j in range(10):
            primes[i][0] in func(bounds[i])
            primes[i][1] in func(bounds[i])
        t = time.clock() - start
        row = [i, t]
        print(row)
        rows.append(row)
        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def compsievetimer(func):
    rows = [['Magnitude', 'Time (sec)']]
    path = r'C:\Users\Kenny\Dropbox\BCA\Senior Year\ToK\%s_composite.csv'%func.__name__
        
    for i in range(len(composites[:9])):
        start = time.clock()
        for j in range(10):
            composites[i][0] in func(bounds[i])
            composites[i][1] in func(bounds[i])
        t = time.clock() - start
        row = [i, t]
        print(row)
        rows.append(row)
        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def ecmtestprimes():
    rows = [['Magnitude', 'Time (sec)']]
    path = r'C:\Users\Kenny\Dropbox\BCA\Senior Year\ToK\ecm_prime.csv'

    for i in range(len(primes)):
        start = time.clock()
        for j in range(100):
            len(list(factors(primes[i][0], False, True, 10, 1))) == 1
            len(list(factors(primes[i][1], False, True, 10, 1))) == 1
        t = time.clock() - start
        row = [i, t]
        print(row)
        rows.append(row)
        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
            
def ecmtestcomps():
    rows = [['Magnitude', 'Time (sec)']]
    path = r'C:\Users\Kenny\Dropbox\BCA\Senior Year\ToK\ecm_composite.csv'

    for i in range(len(primes)):
        start = time.clock()
        for j in range(100):
            len(list(factors(composites[i][0], False, True, 10, 1))) == 1
            len(list(factors(composites[i][1], False, True, 10, 1))) == 1
        t = time.clock() - start
        row = [i, t]
        print(row)
        rows.append(row)
        
        with open(path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)

def trial_div(n):
    if n == 1: return False
    if n == 2 or n == 3 or n == 5: return True
    if n % 2 == 0: return False

    for d in range(3, int(n**0.5)+1):
        if n % d == 0:
            return False

    return True

# following two adapted from 
# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
# original algorithms return smallest prime factor, simply add a test to see if that number is the input to find prime
def pollard_rho(N):
    if N%2==0:
        return 2
    x = random.randint(1, N-1)
    y = x
    c = random.randint(1, N-1)
    g = 1
    while g==1:             
        x = ((x*x)%N+c)%N
        y = ((y*y)%N+c)%N
        y = ((y*y)%N+c)%N
        g = gcd(abs(x-y),N)
    return g == N

def brent(N):
    if N%2==0:
        return 2
    y,c,m = randint(1, N-1),randint(1, N-1),randint(1, N-1)
    g,r,q = 1,1,1
    while g==1:
        x = y
        for i in range(r):
            y = ((y*y)%N+c)%N
        k = 0
        while (k<r and g==1):
            ys = y
            for i in range(min(m,r-k)):
                y = ((y*y)%N+c)%N
                q = q*(abs(x-y))%N
            g = gcd(q,N)
            k = k + m
        r = r*2
    if g==N:
        while True:
            ys = ((ys*ys)%N+c)%N
            g = gcd(abs(x-ys),N)
            if g>1: break
    return g == N

def miller_rabin_pass1(a, n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1

    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def miller_rabin_det(n):
    for a in [2, 3, 5, 7, 11, 13, 17]:
      if not miller_rabin_pass1(a, n):
        return False
    return True

# following two deprecated
# http://programmingpraxis.com/2010/02/02/proving-primality/
def factors_of(n):
    f = 2
    for step in chain([0,1,2,2], cycle([4,2,4,2,4,6,2,6])):
        f += step
        if f*f > n:
            if n != 1:
                yield n
            break
        if n%f == 0:
            yield f
            while n%f == 0:
                n /= f

def lucas(n):
    x = n-1
    if n%2 == 0: 
        return n == 2
    factors = list(factors_of(x))
    b = 2
    while b < n:
        if pow( b, x, n ) == 1:
            for q in factors:
                if pow(b, x/q) % n== 1:
                    break
            else:
                return True
        b += 1
    return False
    
# following two from 
# http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)
def miller_rabin_pass2(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1
    
def miller_rabin_prob(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = randrange(n)
        if not miller_rabin_pass2(a, s, d, n):
            return False
    return True
    
def sieve_eratosthenes(n):
    if n <= 2:
        return []
    sieve = list(range(3, n, 2))
    top = len(sieve)
    for si in sieve:
        if si:
            bottom = (si*si - 3) // 2
            if bottom >= top:
                break
            sieve[bottom::si] = [0] * -((bottom - top) // si)
    return [2] + [el for el in sieve if el]

def sieve_sundaram(limit):
    numbers = list(range(3, limit + 1, 2)) # list of numbers to filter
    limit //= 2 # working limit is half the primes limit
    start = 4

    # generates 'array'
    for diff in range(3, limit + 1, 2): # 3,5,7,9,11...
        for i in range(start, limit, diff):
            numbers[i-1] = 0 # 2*i+1 is at index (i-1) in numbers
        start += 2*(diff+1)

        if start > limit:
            # filters out zeroes and add the prime 2
            return [2] + list(filter(None, numbers))

def sieve_atkin(end):
    assert end > 0
    lng = ((end-1) // 2)
    sieve = [False] * (lng + 1)

    x_max, x2, xd = int(sqrt((end-1)/4.0)), 0, 4
    for xd in range(4, 8*x_max + 2, 8):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not (n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            m = n % 12
            if m == 1 or m == 5:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, x2, xd = int(sqrt((end-1) / 3.0)), 0, 3
    for xd in range(3, 6 * x_max + 2, 6):
        x2 += xd
        y_max = int(sqrt(end-x2))
        n, n_diff = x2 + y_max*y_max, (y_max << 1) - 1
        if not(n & 1):
            n -= n_diff
            n_diff -= 2
        for d in range((n_diff - 1) << 1, -1, -8):
            if n % 12 == 7:
                m = n >> 1
                sieve[m] = not sieve[m]
            n -= d

    x_max, y_min, x2, xd = int((2 + sqrt(4-8*(1-end)))/4), -1, 0, 3
    for x in range(1, x_max + 1):
        x2 += xd
        xd += 6
        if x2 >= end: y_min = (((int(ceil(sqrt(x2 - end))) - 1) << 1) - 2) << 1
        n, n_diff = ((x*x + x) << 1) - 1, (((x-1) << 1) - 2) << 1
        for d in range(n_diff, y_min, -8):
            if n % 12 == 11:
                m = n >> 1
                sieve[m] = not sieve[m]
            n += d

    primes = [2, 3]
    if end <= 3:
        return primes[:max(0,end-2)]

    for n in range(5 >> 1, (int(sqrt(end))+1) >> 1):
        if sieve[n]:
            primes.append((n << 1) + 1)
            aux = (n << 1) + 1
            aux *= aux
            for k in range(aux, end, 2 * aux):
                sieve[k >> 1] = False

    s  = int(sqrt(end)) + 1
    if s  % 2 == 0:
        s += 1
    primes.extend([i for i in range(s, end, 2) if sieve[i >> 1]])

    return primes
