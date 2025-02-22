class student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id

    def display(self):
        print(f'studen: {self.name}, ID: {self.student_id}')


student1 = student('jhondoe', '12345')
student1.display_info()