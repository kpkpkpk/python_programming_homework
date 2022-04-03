import random
import matplotlib.pyplot as plt


def prepare_data():
    arr = [random.randint(1, 100) for _ in range(25)]
    a = arr.pop()
    arr.append(a)
    for i in range(3):
        arr.append(a)
    return arr


new = prepare_data()

# Винзорирование + метод со скользящим окном наблюдения
def sglazh(arr):
    new_arr = [[arr[0], arr[1]]]
    a = 2
    b = 0
    while a < len(arr)-2:
        while ((sum(new_arr[b]) / len(new_arr[b])) / new_arr[b][len(new_arr[b])//2]) < 0.98:
            b += 1
            new_arr.append([arr[a], arr[a + 1]])
            a += 2
        else:
            new_arr[b].append(arr[a])
            a += 1
    new2 = []
    print(new_arr)
    for i in range(len(new_arr)):
        new2.append(sum(new_arr[i])/len(new_arr[i]))
    return new2


new1 = sglazh(new)
new1.insert(0, new[0])


plt.plot([i for i in range(len(new))], new)
plt.show()

plt.plot([i for i in range(len(new1))], new1)
plt.show()


print(new)
print(new1)

if __name__ == '__main__':
    print('main\\n')
