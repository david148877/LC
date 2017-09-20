class Solution:
# @param {integer} n
# @return {integer}
def countPrimes(self, n):
    if n < 3:      #since <n. 1(not prime) and 2(prime, but description ask for <n) 
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])  #list[start:stop:step]
    return sum(primes)
    


'''

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
let`s assume n == 100, we need to count all the primes which are less than 100:
when i == 2:

primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
It will mark out the numbers as none-prime:
4: 100 : 2 ---> 4,6,8,10,12,14 ... 100
which makes prime[4] =False, prime[6]=False, prime[8]=False....

similarly:
when i ==3:
9: 100 : 3 -- > 9,12,15,18,21,24... 96, 99
when i == 4:
16: 100 :4 --> 16,20,24,28.... 96,100
...
...
So if n is not a prime, prime[n] = False, otherwise, prime[n] = True, which is 1 in math.
So sum the whole list, you will get the count of primes.

'''
