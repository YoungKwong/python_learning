#9.1./9.2.
class Student_12(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    
#9.3.
class Student(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender
        
#9.4.
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

def run_twice(animal):
    animal.run()
    animal.run()

#9.5.
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
    
#9.6.
class Student_6(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1  #一个要点是类变量在类内部和外部都应该使用 类名.类变量 的形式访问
