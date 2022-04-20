# Exercise 1
def sum_to(n):
    return sum(range(n+1))

print(sum_to(6))
print(sum_to(10))

# Exercise 2
def largest(numbers):
    largest = 0
    for num in numbers:
        if num > largest:
            largest = num
    return largest

print(largest([1, 2, 3, 4, 0]))
print(largest([10, 4, 2, 231, 91, 54]))

# Exercise 3
def occurances(string, sub):
    return string.count(sub)

print(occurances('fleep floop', 'e'))
print(occurances('fleep floop', 'p'))
print(occurances('fleep floop', 'ee'))
print(occurances('fleep floop', 'fe'))

# Exercise 4
def product(*args):
    total = 1
    for arg in args:
        total = total * arg
    return total

print(product(-1, 4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))