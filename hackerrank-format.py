

def average(student_marks,name):
    a = []
    for i in student_marks:
        if i == name:
            a = sum(student_marks[i])
            b = float(a/(len(student_marks[i])))
            b = format(b,'.2f')
            print(b)


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    average(student_marks,query_name)