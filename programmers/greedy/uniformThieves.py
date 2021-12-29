def solution(n, lost, reserve):
    answer = 0
    student = [_+1 for _ in range(n)]
    student_c = student.copy()

    for j in lost:
        student_c[student.index(j)] = 0

    for i in student_c:
        a = student[student_c.index(i)]
        if (i == 0):
            if a in reserve:
                student_c[student_c.index(i)] = a
                reserve.remove(a)

            elif a - 1 in reserve:
                student_c[student_c.index(i)] = a
                reserve.remove(a - 1)

            elif (a + 1) in reserve:
                student_c[student_c.index(i)] = a
                reserve.remove(a + 1)

    for x in student_c:
        if x == 0:
            student_c.remove(x)

    answer = len(student_c)

    return answer
