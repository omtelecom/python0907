def square_even(n):
    for i in range(2, n + 1 , 2 ):
        i = i ** 2
        print(i)
    return i


print (square_even(7))

