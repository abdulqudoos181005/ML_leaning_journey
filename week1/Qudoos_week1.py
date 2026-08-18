from itertools import product

import numpy as np

#1
a = 3 
b = 4 
print("before swap: ", a ,b)
def swap(x,y):
    return y,x

a,b = swap(a,b)

print("after swap: ",a,b)


#2
def _isprime(n):
    if n < 2:
        return False
    for i in range(2, int(np.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

is_prime = _isprime(6)
print("Is 6 prime?", is_prime)


#3
def febonacci(n):
    if n <= 0:
        return[]
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[i - 1] + fib_sequence[i - 2]
        fib_sequence.append(next_number)
    return fib_sequence


print("Fibonacci sequence for 10 terms:", febonacci(10))


#4
def dup_remove(lst):
    return list(set(lst))

print("Removing duplicates from [1, 2, 2, 3, 4, 4, 5]:", dup_remove([1, 2, 2, 3, 4, 4, 5]))


#5
def multiply(*a):
    result = 1
    for x in a:
        result *= x
    return result

print("Multiplying 2, 3, and 4:", multiply(2, 3, 4))


#6
freq = {w: len(w) for w in ['apple', 'banana', 'cherry'] }
print("Frequencies of words:", freq)


#7
dic = {
    'name' : ['John', 'Jane', 'Doe'],
    'dept' : ['HR', 'Finance', 'IT'],
    'salary' : [50000, 60000, 70000]
}
print (max(dic['salary']))

#8
extracted = lambda x: [i for i in x if i % 2 == 0]
print("Extracted even numbers:", extracted([1, 2, 3, 4, 5, 6]))


np.array([i for i in range(1, 30)])

