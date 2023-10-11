import os
#Check to see if a given number is a prime number. Try to use number theory to solve.
number = int(input("Pass in a number: "))
digits = [int(d) for d in str(number)]



#Do the research on the theory of prime numbers: trial division, Sieve of Eratosthenes, Fermat’s little theorem, Miller-Rabin primality test

#Let's use a combination of methods and define some requirements around input

#Check if number is > 100
assert 0 <= number <= 100
#Create an initial list of primes, including the false positive under 100
primes = [2, 3, 5, 7, 11, 13, 17, 19, 49, 91]
conditions = {
    number == 0: "",
    number not in primes: "",
    0 not in [number % p for p in primes]: "",
    sum(digits) % 3 != 0: "",
    digits[-1] not in [0, 2, 4, 5, 6, 8]: "",
}

if all(condition for condition in conditions.keys()):
    print("{0} is a prime number".format(number))
else:
    print("{0} is not a prime number".format(number))


#Exercise: Instead of checking for all conditions, call the condition that matches the input and output a message. Messages for each condition can be contained within the double quotes
