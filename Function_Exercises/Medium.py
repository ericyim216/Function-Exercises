#1. Find the smallest number
num = [1, 22, 333, 4444]
def smallest():
    print('Smallest number is: ', min(num))
smallest()

#2. Find the largest number
def largest():
    print('Largest number is: ', max(num))
largest()

#3. Shortest String
strings = ['short', 'notshort', 'longerthanshort']
def shorteststring():
    print('Shortest string is: ', min(strings, key=len))
shorteststring()

#4. Longest String
def longeststring():
    print('Longest string is: ', max(strings, key=len))
longeststring()