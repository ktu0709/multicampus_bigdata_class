class Human:
    def __init__(self, name, age, height, weight) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def printInformation(self):
        return f'이름: {self.name}, 나이: {self.age}, 키: {self.height}, \n몸무게: {self.weight}, '

class Student(Human):
    def __init__(self, name, age, height, weight, number, major) -> None:
        super().__init__(name, age, height, weight)
        self.number = number
        self.major = major

    def printInformation(self):
        return super().printInformation() + f'학번: {self.number}, 전공: {self.major}' + '\n'

if __name__ == '__main__':
    students = [
        Student('홍길동', 15, 171, 81, '201101', '영문'),
        Student('한사람', 13, 183, 72, '201102', '건축'),
        Student('임걱정', 16, 175, 65, '201193', '무용')
    ]
    for student in students:
        print(student.printInformation())