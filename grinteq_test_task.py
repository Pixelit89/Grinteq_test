# class Student(object):
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name



student1 = {
    'first_name': 'Alex',
    'last_name': 'Bus',
    'subjects': {
        'rabbit breeding':{
            'rate': 5,
            'exam': 1
        },
        'quantum mechanics': {
            'rate': 4,
            'exam': 6
        },
        'math': {
            'rate': 3,
        },
        'english': {
            'rate': 5,
            'exam': 7
        }
    }
}

student2 = {
    'first_name': 'Bob',
    'last_name': 'Well',
    'subjects': {
        'rabbit breeding':{
            'rate': 1,
            'exam': 5
        },
        'quantum mechanics': {
            'rate': 9,
            'exam': 3
        },
        'math': {
            'rate': 9,
            'exam': 4
        },
        'english': {
            'rate': 9,
            'exam': 10
        }
    }
}

student3 = {
    'first_name': 'Pit',
    'last_name': 'Bull',
    'subjects': {
        'rabbit breeding':{
            'rate': 3,
            'exam': 6
        },
        'quantum mechanics': {
            'rate': 9,
            'exam': 6
        },
        'math': {
            'rate': 1,
            'exam': 6
        },
        'english': {
            'rate': 9,
            'exam': 10
        }
    }
}

student4 = {
    'first_name': 'George',
    'last_name': 'Brown',
    'subjects': {
        'rabbit breeding':{
            'rate': 3,
            'exam': 6
        },
        'quantum mechanics': {
            'rate': 9,
            'exam': 3
        },
        'math': {
            'rate': 9,
        },
        'english': {
            'rate': 9,
            'exam': 10
        }
    }
}

student5 = {
    'first_name': 'Clara',
    'last_name': 'Heinz',
    'subjects': {
        'rabbit breeding':{
            'rate': 3,
            'exam': 6
        },
        'quantum mechanics': {
            'rate': 9,
            'exam': 3
        },
        'math': {
            'rate': 9,
        },
        'english': {
            'rate': 9,
            'exam': 10
        }
    }
}


class Gradebook(object):
    student_list = []

    @classmethod
    def get_best_exam_student(cls, subject):
        best_student = max(cls.student_list, key=lambda x: x['subjects'][subject]['exam'] if 'exam' in x['subjects'][subject] else False)
        return best_student

    @classmethod
    def get_passed_exams(cls):
        passed_exams = []
        for student in cls.student_list:
            for subject in student['subjects']:
                if 'exam' in student['subjects'][subject] and not subject in passed_exams:
                    passed_exams.append(subject)
        return passed_exams

    @classmethod
    def print_result_grades(cls):
        for student in cls.student_list:
            print(student['last_name'])
            for subject in student['subjects']:
                if 'exam' in student['subjects'][subject]:
                    result_grade = round(student['subjects'][subject]['rate']*0.3 +\
                                   student['subjects'][subject]['exam']*0.7)
                    print("\t{0} - {1}".format(subject, result_grade))


Gradebook.student_list.append(student1)
Gradebook.student_list.append(student2)
Gradebook.student_list.append(student3)


print(Gradebook.get_best_exam_student('math'))
print(Gradebook.get_passed_exams())
Gradebook.print_result_grades()