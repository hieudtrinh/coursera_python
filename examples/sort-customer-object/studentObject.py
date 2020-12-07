import sys


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))


def main(argv, arc):
    student_objects = [
        Student('john', 'A', 15),
        Student('jane', 'B', 12),
        Student('dave', 'B', 10),
    ]


    # list.sort() sort the list in place
    print('Unsorted list ')
    print(student_objects)
    # sorted() built in function return the sorted list
    print('sorted(list) return sorted list')
    print(sorted(student_objects, key=lambda student: student.age))


    # list.sort() sort the list in place
    print('Unsorted list ')
    print(student_objects)
    student_objects.sort(key=lambda student: student.name)
    print('list.sort() sorted the list by name in place ')
    print(student_objects)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
