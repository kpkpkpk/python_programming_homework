from random import randint

def approx(s, f, arr):
    k = 0
    b = 0
    if f == len(arr):
        f -= 1
    if arr[f] == None:
        k = arr[s - 1] - arr[s - 2]
        b = arr[s - 1] - k * (s - 1)
        
    else:
        if s == 0:
           b = arr[f]
        else:
            k = (arr[f] - arr[s - 1])/(f - s + 1)
            b = arr[s - 1] - k * (s - 1)
    for i in range(s, f):
        arr[i] = int(k*i + b)
    if arr[f] == None:
        arr[f] = int(k*f + b)


array = [randint(1, 10) for i in range(100)]

for i in range(10):
    array[randint(0, len(array))] = randint(1000, 2000)
print(array)

i = 0
s = 0
f = 0
while i < len(array):
    while i < len(array) and array[i] >= 1000:
        array[i] = None
        i += 1 
        f = i 
    if s != f:
        approx(s, f, array)

    i += 1
    s = i
    f = i
print(array)