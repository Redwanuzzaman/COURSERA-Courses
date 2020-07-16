# 1 

def factorial(n):
    result = 1
    for x in range(1, n+1):
        result = result * x
    return result

for n in range(0, 10):
    print(n, factorial(n))


# 2

for num in range(1, 11):
  print(num ** 3)
  
  
# 3

for i in range(0, 100, 7):
    print(i)
