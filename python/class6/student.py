class Student:
    def __init__(self, name, age, school):
        self.name = name
        self.age = age
        self.school = school
        self.scores = []

    def take_exam(self, score):
        self.scores.append(score)

    def get_score_average(self):
        print('student get_score_average')
        if len(self.scores) == 0:
            return -1
        else:
            return sum(self.scores) // len(self.scores)

    def get_grade(self):
        average = self.get_score_average()

        if average < 0:
            return 'N/A'
        if average >= 90:
            return 'A'
        if average >= 80:
            return 'B'
        if average >= 70:
            return 'C'
        if average >= 60:
            return 'D'
        return 'F'

    def report(self):
        print(self.name)
        print(self.scores)
        print(self.get_grade())

class Graduate(Student):
    def get_score_average(self):
        print('graduate get_score_average')
        if len(self.scores) <= 1:
            return super().get_score_average()

        calc_scores = list(self.scores)
        calc_scores.remove(min(calc_scores))
        return sum(calc_scores) // len(calc_scores)
        
    def get_grade(self):
        grade = super().get_grade()
        if grade != 'N/A' and grade != 'F':
            return 'P'
        return grade
    
##        average = self.get_score_average()
##
##        if average < 0:
##            return 'N/A'
##        if average >= 60:
##            return 'P'
##        return 'F'

if __name__ == '__main__':
##    john = Student('John', 17, 'San Jose State')
##    john.take_exam(100)
##    john.take_exam(82)
##    john.take_exam(75)
##    print(john.get_score_average())
##    print(john.get_grade())
##    john.report()
    
    jack = Graduate('Jack', 22, 'Berkeley')
    jack.take_exam(100)
    jack.take_exam(62)
    jack.take_exam(5)
    #print(jack.get_score_average())
    print(jack.get_grade())
    jack.report()
