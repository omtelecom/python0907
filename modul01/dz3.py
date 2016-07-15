def index_power(list, n):
    return list[n]**n if 0 <= n < len(list) else -1
list  = [1, 3, 10, 100]
print (index_power(list, 3))