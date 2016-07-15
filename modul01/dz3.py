def square_even(n):
    list = [i * i for i in range(2, n + 1 ) if i % 2 == 0]
    return list

print (square_even(6))
