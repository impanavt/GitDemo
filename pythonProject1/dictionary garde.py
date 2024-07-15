student_marks={'Jerry':92,
               'Harry':78,
               'Dimpy':56,
                'Rahul':41,
                 'Aniket':99
               'impana':100
}
student_grades={}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grades[student]="A+"
    elif marks>80:
        student_grades[student]='A'
    elif marks>70:
        student_grades[student]='B+'
    elif marks>50:
        student_grades[student]='B'
print(student_grades)