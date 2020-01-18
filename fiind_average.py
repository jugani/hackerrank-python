avaerage_valuefrom functools import reduce
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
 
student_marks_list = (student_marks[query_name])
sum = reduce(lambda a, b: a + b , student_marks_list )/3
avaerage_value = round(sum,2)
print ("%.2f" % avaerage_value)  
# print(avaerage_value)