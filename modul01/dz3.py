def index_power(array, n):
    return array[n]**n if 0 <= n < len(array) else -1
array  = [1, 3, 10, 100]
print (index_power(array, 3))