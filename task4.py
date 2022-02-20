from math import pow

# количество дней для вероятности n
C = 4
# количество дней для определения вероятности только у одного студента
D = 4 + 400
# Хранение учеников будет в мапе <String, Float>, где K - имя, а V - вероятность за C дней
students = dict()


def find_solution(name: str, dictionary: dict):
    answer = 1
    for dict_name in dictionary.keys():
        if dict_name == name:
            answer *= pow((1 - dictionary[dict_name]), D)
        else:
            answer *= pow(dictionary[dict_name], D)
    print(answer)


if __name__ == '__main__':
    # количество третьекурсников
    print("Введите количество третьекурсников:")
    num_of_students = int(input())
    # событие
    print("Какое событие чаще всего с ними случается?")
    event = input()
    print("Вводите студента в формате: name вероятность(указывать через точку)")
    for i in range(num_of_students):
        key, value = map(str, input().split(" "))
        # находим сразу же вероятность того, что событие не наступит (Формула x=sqrt^C(1-p))
        students[key] = pow(1 - float(value), (1 / C))
        print(students[key])
    print("Введите имя студента, которого вы хотите увидеть:")
    required_student = input()
    find_solution(required_student, students)
