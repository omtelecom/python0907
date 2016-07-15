def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0 :
        a = 'Fizz Buzz'
    elif number % 3 == 0:
        a = 'Fizz'
    elif number % 5 == 0:
        a = 'Buzz'
    else:
        a = str(number)
    return a

print (fizzbuzz(15))
print (fizzbuzz(6))
print (fizzbuzz(5))
print (fizzbuzz(7))
