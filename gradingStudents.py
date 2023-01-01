def gradingStudents(grades):
    return [(i+5-(i%5)) if (i%5>2 and i>=38) else i for i in grades]
