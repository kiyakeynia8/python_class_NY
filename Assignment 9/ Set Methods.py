import random

while True:
    numbers = {0}
    r = random.randint(1, 50)
    o = 0
    e = 0

    for i in range(r):
        n = random.randint(0, 100)
        numbers.add(n)
    
    print(numbers)

    numbers_c = numbers.copy()
    
    for i in range(len(numbers_c)):
        if list(numbers_c)[i] % 2 != 0:
            o += 1
        else:
            e += 1
    
    if o > e:
        numbers_c.clear()
    else:
        for i in range(len(numbers_c)):
            if i >= len(numbers_c):
                break
            if list(numbers_c)[i] % 2 != 0:
                numbers_c.remove(list(numbers_c)[i])
                # or
                # numbers_c.discard(numbers_c[i])
        
        numbers.update(numbers_c)
        break

print(numbers)