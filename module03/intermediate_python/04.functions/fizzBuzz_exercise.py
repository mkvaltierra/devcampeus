"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the 
number and for the multiples of five print "Buzz". For
numbers which are multiples of both three and five print
"FizzBuzz"

Have to use: 
- function
- looping
- conditionals
- Math operators
"""

def fizzbuzz(max_value):

    number_list = range(1, max_value + 1)
    
    for number in number_list:
        if (number % 3 == 0 and number % 5 == 0):
            print('FizzBuzz')
        elif number % 5 == 0:
            print('Buzz')
        elif number % 3 == 0:
            print('Fizz')
        else:
            print(number)
            
        
    

fizzbuzz(100)