#1. Madlib function
def madlib(name, subject):
    print("%s's favorite subject is %s." % (name, subject))
name = input("Enter a name ")
subject = input("Enter a subject ")
madlib(name, subject)
#def madlib(name="Eric",subject="Sub"):
#   print("%s's favorite subject is %s" % (name,subject))
#   madlib("John","Math")

#2. Celsius to Fahrenheit conversion
def f_to_c(f):
    c = (f - 32) * 5/9
    return c
c = int(input("Input a temperture\n"))
print(c, "°F is equal to: ", f_to_c(c), "°C")


# #3. Fahrenheit to Celsius conversion
def c_to_f(c):
    f = (c * 9/5) + 32
    return f
f = int(input("Input a temperture\n"))
print(f, "°C is equal to: ", c_to_f(f), "°F")

#4. is_even function
def even(num):
    res = False
    if num % 2 == 0:
        res = True
    return res
print(even(2))
print(even(3))

#5. is_odd function
def odd(num):
    res = True
    if num % 2 == 0:
        res = False
    return res
print(odd(2))
print(odd(3))

#6. only_evens
def evens(list):
    even_list = []
    for i in list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list
print(evens([11, 20, 42, 97, 23, 10]))

#7. only_odds
def odds(list):
    odd_list = []
    for i in list:
        if i % 2 != 0:
            odd_list.append(i)
    return odd_list
print(odds([11, 20, 42, 97, 23, 10]))
