# n = 5
# student_marks = {}
# for i in range(n):
#     name *line= input()
#     scores = list(map(float, line))
#     student_marks[name] = scores
# query_name = input()

#1
# w = [3,4,5,1] 
# k = [5]  
# def example(sum):
#     return sum*2
# print(list(map(example,w)))

# #2
# s = "hi" #["hello","how", "hi"]
# s1 = ["hello","how"]
# def example2(sum):
#     return sum+s
# print(list(map(example2,s1)))


# a =["34","23","45"]

# print(list(map(str,w)))
# print(list(map(int,a)))


# if __name__ == '__main__': 
#     print("Enter number of students: \n")
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         print("Enter student name and marks \n")
#         name, *line = input().split()
#         print(student_marks) 
        
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     print(student_marks) 
#3 lamnada
numbers = (1, 2, 3, 4)
result = list(map(lambda x: x*x, numbers))
print("result is",result)

# converting map object to set
# d = {}

# print(numbersSquare)
# len(numbers)
# for x in range(0,len(numbers)):
#     d[]= x

# 4) multiple parameters

num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda *args: args, num1, num2)
print(list(result))


