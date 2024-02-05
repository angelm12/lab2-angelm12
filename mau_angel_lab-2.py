# 1.1 Write a function that takes a year as input and returns whether the year is a leap year or not.

# Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, but these centurial years are leap years if they are exactly divisible by 400. 

# Input: 2000
# Output: True

# Input: 1900
# Output: False

# Input: 2004
# Output: True

# Input: 2019
# Output: False

def leap_check(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    return False

print("Leap checks:", leap_check(2000), leap_check(1900), leap_check(2004), leap_check(2019))
 

# 1.2 Write a function that takes a list of numbers as input, and returns the median of the list

# If the sorted list has an odd number of elements, the median is the middle element. If the list has an even number of elements, the median is the average of the two middle elements.

# Input: [3, 1, 5, 7, 8, 9, 4]
# Output: 5

# Input: [3, 1, 4, 1, 5, 9, 2]
# Output: 3
def median(elem):
    elem.sort()
    n = len(elem)
    mid = n // 2
    if n % 2 == 0:
        return (elem[mid - 1] + elem[mid]) / 2
    else:
        return elem[mid]

print("median check1:", median([3, 1, 5, 7, 8, 9, 4]))
print("median check2:", median([3, 1, 5, 7, 8, 9, 4]))






# 1.3 Write a function that takes a string as input and returns only the consonants from the word as a string

# Input:"luguburious"
# Output: "lgbrs"
def consonants(string):
    vowels = 'aeiou'
    output = ''
    
    for letter in string:
        if letter.isalpha() and letter.lower() not in vowels:
            output += letter
        return output

print("constonant test: ", consonants("luguburious"))


# 1.4 Write a function that takes a list of numbers as input and returns the standard deviation 

# Formula: Standard deviation formula

# Input: [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
# Output: 2.8722813232690143
def stardard_dev(input):

    mean = sum(input) / len(input)
    
    sum_of_squared_differences = 0
    
    for num in input:
        squared_difference = (num - mean) ** 2  
        sum_of_squared_differences += squared_difference 
    
    var = sum_of_squared_differences / len(input)
    return var ** 0.5

print("standard deviation test: ", stardard_dev([30, 31, 32, 33, 34, 35, 36, 37, 38, 39]))
 

# 1.5 Write a function that takes a list of names as input and returns a combination of names as output 

# Input: ['Andrea', 'Bob', 'Cassandra', 'Doug']
# Output: [('Andrea', 'Bob'), ('Andrea', 'Cassandra'), ('Andrea', 'Doug'), ('Bob', 'Cassandra'), ('Bob', 'Doug'), ('Cassandra', 'Doug')]
def combinations_names(names):
    combs = []
    
    
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            combs.append((names[i], names[j]))
    
    return combs
print("combinations tests: ", combinations_names(['Andrea', 'Bob', 'Cassandra', 'Doug']))