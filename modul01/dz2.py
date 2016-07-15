def square_even(n):
    for i in range(2, n + 1 ):
        if i % 2 == 0:
            print(i ** 2)
    return i


print (square_even(7))

